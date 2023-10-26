[Setup]
AppName=PowerModule
AppVerName=PM 1.0
DefaultDirName=D:\Github\PowerModule
DefaultGroupName=PowerModule
OutputDir=Output
OutputBaseFilename=PowerModuleSetup
Compression=lzma
SolidCompression=yes
AppCopyright=Copyright © 2023
AppPublisher=https://github.com/Vabolos/PowerModule
DefaultUserInfoName=LucFrankhuizen
DefaultUserInfoOrg=NorthDevs
DefaultUserInfoSerial=12345-67890
OutputManifestFile=Output\powermodule.exe.manifest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:";

[Files]
Source: "D:\Github\PowerModule\*"; DestDir: "{app}"; Flags: ignoreversion
; Add any other necessary files

[Icons]
Name: "{group}\PowerModule"; Filename: "{app}\powermodule.ico"
Name: "{commondesktop}\PowerModule"; Filename: "{app}\powermodule.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\GUI.py"; Description: "Launch My App"; Flags: postinstall shellexec skipifsilent

[Code]
function NextButtonClick(CurPageID: Integer): Boolean;
begin
  if CurPageID = wpWelcome then
  begin
    MsgBox('Welcome to PowerModule Setup', mbInformation, MB_OK);
  end;
  Result := True;
end;
