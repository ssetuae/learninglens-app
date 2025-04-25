"""
Domain and SSL configuration for Render deployment
"""

import os

def get_render_config():
    """
    Generate configuration for Render deployment
    """
    return {
        "name": "learninglens",
        "env": "python",
        "buildCommand": "pip install -r requirements.txt",
        "startCommand": "gunicorn wsgi:application",
        "envVars": [
            {"key": "FLASK_ENV", "value": "production"},
            {"key": "SECRET_KEY", "value": "{{ .Secrets.SECRET_KEY }}"},
            {"key": "DATABASE_URL", "value": "{{ .Secrets.DATABASE_URL }}"},
            {"key": "MAIL_USERNAME", "value": "{{ .Secrets.MAIL_USERNAME }}"},
            {"key": "MAIL_PASSWORD", "value": "{{ .Secrets.MAIL_PASSWORD }}"},
            {"key": "ADMIN_EMAIL", "value": "helpdesk@shiningstaronline.com"}
        ],
        "healthCheckPath": "/",
        "autoDeploy": True,
        "domains": ["learninglens.shiningstaronline.com"]
    }

def generate_render_yaml():
    """
    Generate render.yaml file for Render Blueprint deployment
    """
    render_yaml = """
services:
  - type: web
    name: learninglens
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn wsgi:application
    envVars:
      - key: FLASK_ENV
        value: production
      - key: SECRET_KEY
        sync: false
      - key: DATABASE_URL
        fromDatabase:
          name: learninglens-db
          property: connectionString
      - key: MAIL_USERNAME
        sync: false
      - key: MAIL_PASSWORD
        sync: false
      - key: ADMIN_EMAIL
        value: helpdesk@shiningstaronline.com
    healthCheckPath: /
    autoDeploy: true

databases:
  - name: learninglens-db
    databaseName: learninglens
    user: learninglens_user
    plan: starter
"""
    
    with open('render.yaml', 'w') as f:
        f.write(render_yaml)
    
    print("Generated render.yaml for Render Blueprint deployment")

def setup_custom_domain_instructions():
    """
    Generate instructions for setting up a custom domain on Render
    """
    instructions = """
# Setting up a Custom Domain on Render

After deploying your application to Render, follow these steps to configure your custom domain:

## 1. Add Your Domain in Render Dashboard

1. Log in to your Render dashboard
2. Select your LearningLens web service
3. Go to the "Settings" tab
4. Scroll down to the "Custom Domain" section
5. Click "Add Custom Domain"
6. Enter your domain: learninglens.shiningstaronline.com
7. Click "Save"

## 2. Configure DNS Records

Add the following DNS records to your domain provider's dashboard:

### Option 1: CNAME Record (Recommended)
- Type: CNAME
- Name: learninglens
- Value: [Your Render URL].onrender.com
- TTL: 3600 (or default)

### Option 2: A Records
If your DNS provider doesn't support CNAME records at the root domain, use these A records:
- Type: A
- Name: learninglens
- Value: 76.76.21.21
- TTL: 3600 (or default)

## 3. Verify and Wait for SSL Certificate

- Render will automatically provision an SSL certificate for your domain
- This process can take up to 24 hours
- You can check the status in the "Custom Domain" section of your service settings

## 4. Test Your Custom Domain

Once the SSL certificate is issued, visit your custom domain to verify it's working:
https://learninglens.shiningstaronline.com
"""
    
    with open('custom_domain_setup.md', 'w') as f:
        f.write(instructions)
    
    print("Generated custom domain setup instructions")

def main():
    generate_render_yaml()
    setup_custom_domain_instructions()

if __name__ == "__main__":
    main()
