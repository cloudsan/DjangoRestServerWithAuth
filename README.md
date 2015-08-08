# RestServerAuth
        Use Django REST Framework, with basic oauth2, google login, facebook login. 



#in order to regenerate cordova relative files
        #!/bin/bash
        textReset=$(tput sgr0)
        textGreen=$(tput setaf 2)
        message_info () {
          echo "${textGreen}[my-app]${textReset} $1"
        }

        message_info "Creating necessary directories..."
        mkdir plugins
        mkdir platforms

        message_info "Adding platforms..."
        cordova build android
        cordova build ios

        message_info "Adding plugins..."

# If using cordova, change to: cordova plugin add
        cordova plugin add https://git-wip-us.apache.org/repos/asf/cordova-plugin-device.git

# Required dependencies
        pip3 install python-social-auth
        pip3 install djangorestframework
        pip3 install django-cors-headers
        pip3 install django-oauth-toolkit python-social-auth

# Reference
    http://httplambda.com/a-rest-api-with-django-and-oauthw-authentication/
