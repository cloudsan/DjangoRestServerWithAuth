# Required dependencies
sudo -H pip3 install python-social-auth
sudo -H pip3 install djangorestframework
sudo -H pip3 install django-cors-headers

# RestServerAuth
Use Django REST Framework, with basic oauth2



in order to regenerate cordova relative files

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
