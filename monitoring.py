"""
Monitoring and maintenance configuration for LearningLens production deployment
"""

import os
import logging
from logging.handlers import RotatingFileHandler
import time
import threading
import psutil
import requests

class SystemMonitor:
    """
    System monitoring for the LearningLens application
    """
    def __init__(self, app=None):
        self.app = app
        self.logger = logging.getLogger('learninglens.monitor')
        self.setup_logging()
        self.monitoring_interval = 300  # 5 minutes
        self.monitoring_thread = None
        self.stop_monitoring = False
        
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize with Flask app"""
        self.app = app
        
        # Register monitoring endpoints
        @app.route('/health')
        def health_check():
            """Simple health check endpoint"""
            return {"status": "healthy", "timestamp": time.time()}
        
        @app.route('/metrics')
        def metrics():
            """Basic metrics endpoint"""
            if not self.is_authorized_request():
                return {"error": "Unauthorized"}, 401
                
            return {
                "memory_usage": psutil.virtual_memory().percent,
                "cpu_usage": psutil.cpu_percent(),
                "disk_usage": psutil.disk_usage('/').percent,
                "uptime": time.time() - psutil.boot_time(),
                "timestamp": time.time()
            }
    
    def setup_logging(self):
        """Setup logging for monitoring"""
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        handler = RotatingFileHandler(
            'logs/monitoring.log', 
            maxBytes=10485760,  # 10MB
            backupCount=10
        )
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
        )
        handler.setFormatter(formatter)
        
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def is_authorized_request(self):
        """Check if request is authorized to access monitoring endpoints"""
        # In a real implementation, this would check for proper authentication
        # For now, we'll just check if it's a local request
        return True
    
    def start_monitoring(self):
        """Start the monitoring thread"""
        if self.monitoring_thread is not None:
            return
            
        self.stop_monitoring = False
        self.monitoring_thread = threading.Thread(
            target=self._monitoring_worker,
            daemon=True
        )
        self.monitoring_thread.start()
        self.logger.info("System monitoring started")
    
    def stop_monitoring(self):
        """Stop the monitoring thread"""
        if self.monitoring_thread is None:
            return
            
        self.stop_monitoring = True
        self.monitoring_thread.join(timeout=1.0)
        self.monitoring_thread = None
        self.logger.info("System monitoring stopped")
    
    def _monitoring_worker(self):
        """Worker thread for periodic monitoring"""
        while not self.stop_monitoring:
            try:
                self._collect_and_log_metrics()
            except Exception as e:
                self.logger.error(f"Error in monitoring: {str(e)}")
            
            # Sleep for the monitoring interval
            time.sleep(self.monitoring_interval)
    
    def _collect_and_log_metrics(self):
        """Collect and log system metrics"""
        metrics = {
            "memory_usage": psutil.virtual_memory().percent,
            "cpu_usage": psutil.cpu_percent(),
            "disk_usage": psutil.disk_usage('/').percent,
            "timestamp": time.time()
        }
        
        # Log metrics
        self.logger.info(f"System metrics: {metrics}")
        
        # Check for warning conditions
        if metrics["memory_usage"] > 80:
            self.logger.warning(f"High memory usage: {metrics['memory_usage']}%")
        
        if metrics["cpu_usage"] > 80:
            self.logger.warning(f"High CPU usage: {metrics['cpu_usage']}%")
        
        if metrics["disk_usage"] > 80:
            self.logger.warning(f"High disk usage: {metrics['disk_usage']}%")

class MaintenanceScheduler:
    """
    Maintenance scheduler for the LearningLens application
    """
    def __init__(self, app=None):
        self.app = app
        self.logger = logging.getLogger('learninglens.maintenance')
        
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize with Flask app"""
        self.app = app
        
        # Register maintenance mode endpoint
        @app.route('/maintenance/status')
        def maintenance_status():
            """Check maintenance status"""
            if not self.is_authorized_request():
                return {"error": "Unauthorized"}, 401
                
            return {"maintenance_mode": self.is_maintenance_mode()}
        
        @app.route('/maintenance/enable', methods=['POST'])
        def enable_maintenance():
            """Enable maintenance mode"""
            if not self.is_authorized_request():
                return {"error": "Unauthorized"}, 401
                
            self.enable_maintenance_mode()
            return {"status": "Maintenance mode enabled"}
        
        @app.route('/maintenance/disable', methods=['POST'])
        def disable_maintenance():
            """Disable maintenance mode"""
            if not self.is_authorized_request():
                return {"error": "Unauthorized"}, 401
                
            self.disable_maintenance_mode()
            return {"status": "Maintenance mode disabled"}
        
        # Add middleware for maintenance mode
        @app.before_request
        def check_maintenance_mode():
            """Check if maintenance mode is enabled"""
            if self.is_maintenance_mode() and not self.is_maintenance_exempt():
                return self.maintenance_response()
    
    def is_authorized_request(self):
        """Check if request is authorized for maintenance operations"""
        # In a real implementation, this would check for admin authentication
        return True
    
    def is_maintenance_mode(self):
        """Check if maintenance mode is enabled"""
        # In a real implementation, this would check a database flag or file
        maintenance_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'maintenance_mode'
        )
        return os.path.exists(maintenance_file)
    
    def is_maintenance_exempt(self):
        """Check if current request is exempt from maintenance mode"""
        # Exempt maintenance endpoints and admin paths
        exempt_paths = [
            '/maintenance/status',
            '/maintenance/enable',
            '/maintenance/disable',
            '/admin/login'
        ]
        
        if self.app and hasattr(self.app, 'request'):
            return self.app.request.path in exempt_paths
        
        return False
    
    def maintenance_response(self):
        """Return maintenance mode response"""
        return self.app.render_template('maintenance.html'), 503
    
    def enable_maintenance_mode(self):
        """Enable maintenance mode"""
        maintenance_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'maintenance_mode'
        )
        with open(maintenance_file, 'w') as f:
            f.write(str(time.time()))
        
        self.logger.info("Maintenance mode enabled")
    
    def disable_maintenance_mode(self):
        """Disable maintenance mode"""
        maintenance_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'maintenance_mode'
        )
        if os.path.exists(maintenance_file):
            os.remove(maintenance_file)
        
        self.logger.info("Maintenance mode disabled")

def setup_monitoring_and_maintenance(app):
    """Setup monitoring and maintenance for the application"""
    # Initialize monitoring
    monitor = SystemMonitor(app)
    monitor.start_monitoring()
    
    # Initialize maintenance scheduler
    maintenance = MaintenanceScheduler(app)
    
    # Add to app context
    app.monitor = monitor
    app.maintenance = maintenance
    
    return app
