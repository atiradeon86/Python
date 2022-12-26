param (
  
[Parameter(Mandatory=$false)] 
[string]$hostname,

[Parameter(Mandatory=$false)] 
[string]$xml

)

if ($xml) {

$credential = Import-CliXml -Path "$xml"

#Reading passwrod, and username from XML file for the RDP connection
$password = $credential.GetNetworkCredential().password
$username = $credential.username


#Skip Cert CACCheck
$PSSessionOption = New-PSSessionOption -SkipCACheck 

#Create new session
New-PSSession  -ComputerName $hostname -Credential $credential -UseSSL -SessionOption $PSSessionOption

#Get new session ID
$session = Get-PSSession
$id = $session.id

#Enter PSSession
Enter-PSSession $id

} else {

Write-Host "`nPlease provide the required data:`n"
      
#Data request
$username = Read-host "Username"
$password = Read-host "Password" 

Write-Host "`nThe new credential file created, and ready to use : $username.xml" -ForegroundColor Green 

#Password Convert to SecureString
$pw = ConvertTo-SecureString $password -AsPlainText -Force

#Creating the credential xml file
$cred = New-Object System.Management.Automation.PSCredential ($username, $pw)
$cred | Export-CliXml -Path .\$username.xml

$credential = Import-CliXml -Path "$username.xml"

#Reading passwrod, and username from XML file for the RDP connection
$password = $credential.GetNetworkCredential().password
$username = $credential.username

#Skip Cert CACCheck
$PSSessionOption = New-PSSessionOption -SkipCACheck 

#Create new session
New-PSSession  -ComputerName $hostname -Credential $credential -UseSSL -SessionOption $PSSessionOption

#Get new session ID
$session = Get-PSSession
$id = $session.id

#Enter PSSession
Enter-PSSession $id
}