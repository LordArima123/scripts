echo "Accessing PS script"
echo "Installing Module"
Install-Module -Name UIAutomation -Force -AllowClobber -Scope CurrentUser
Import-Module UIAutomation
$installerProcess = Start-Process -FilePath ".\Driver\XPrinter.exe" -PassThru