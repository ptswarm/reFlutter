import pkg_resources
from io import BytesIO
import re
import sys
import csv
import string
import os
import os.path
from os.path import join
from zipfile import ZipFile
import shutil

if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

IPBurp = '192.168.1.12'
libAppArm64 = '',''
libAppArm = '',''
libAppX64 = '',''
libAppX86 = '',''
libios = '',''
libappHash = ''

def silentremove(filename):
    try:
        os.remove(filename)
    except:
        pass

def patchLibrary():
 if len(libios[1]) != 0:
    buffer = open('Flutter', 'rb').read().replace(b'192.168.133.104', IPBurp.encode('ascii'))
    open('Flutter', 'wb').write(buffer)
 if len(libAppArm64[1]) != 0:
    buffer = open('libflutter_arm64.so', 'rb').read().replace(b'192.168.133.104', IPBurp.encode('ascii'))
    open('libflutter_arm64.so', 'wb').write(buffer)
 if len(libAppArm[1]) != 0:
    buffer = open('libflutter_arm.so', 'rb').read().replace(b'192.168.133.104', IPBurp.encode('ascii'))
    open('libflutter_arm.so', 'wb').write(buffer)
 if len(libAppX64[1]) != 0:
    buffer = open('libflutter_x64.so', 'rb').read().replace(b'192.168.133.104', IPBurp.encode('ascii'))
    open('libflutter_x64.so', 'wb').write(buffer)

def inputIPBurp():
    global IPBurp
    try:
        IPBurp = raw_input("Example: (192.168.1.154) etc.\nPlease enter your Burp IP: ")
        if not re.match(r'[0-9]+(?:\.[0-9]+){3}', IPBurp):
            print("Invalid IP Address")
            inputIPBurp()
    except:
        IPBurp = input('Example: (192.168.1.154) etc.\nPlease enter your Burp IP: ')
        if not re.match(r'[0-9]+(?:\.[0-9]+){3}', IPBurp):
            print("Invalid IP Address")
            inputIPBurp()
    IPBurp='.'.join(i.zfill(3) for i in IPBurp.split('.'))

def networkLib():
    global libAppArm64,libAppArm,libAppX64,libAppX86,libios
    if len(libios[1]) != 0:
       try:
        urlretrieve("https://github.com/ptswarm/reFlutter/releases/download/ios-"+libios[1]+"/Flutter", "Flutter")
       except:
        libios='',''
        silentremove("Flutter")
    if len(libAppArm64[1]) != 0:
       try: 
        urlretrieve("https://github.com/ptswarm/reFlutter/releases/download/android-"+libAppArm64[1]+"/libflutter_arm64.so", "libflutter_arm64.so")
       except:
        libAppArm64='',''
        silentremove("libflutter_arm64.so")
    if len(libAppArm[1]) != 0:
       try:
        urlretrieve("https://github.com/ptswarm/reFlutter/releases/download/android-"+libAppArm[1]+"/libflutter_arm.so", "libflutter_arm.so")
       except:
        libAppArm='',''
        silentremove("libflutter_arm.so")
    if len(libAppX64[1]) != 0:
       try:
        urlretrieve("https://github.com/ptswarm/reFlutter/releases/download/android-"+libAppX64[1]+"/libflutter_x64.so", "libflutter_x64.so")
       except:
        libAppX64='',''
        silentremove("libflutter_x64.so")
    if len(libAppX86[1]) != 0:
       try:
        urlretrieve("https://github.com/ptswarm/reFlutter/releases/download/android-"+libAppX86[1]+"/libflutter_x86.so", "libflutter_x86.so")
       except:
        libAppX86='',''
        silentremove("libflutter_x86.so")
    patchLibrary()

def replaceLibFlutter():
    if len(sys.argv) < 3:
        inputIPBurp()
        networkLib()
    if os.path.exists("libflutter_arm64.so") or os.path.exists("libflutter_arm.so") or os.path.exists("libflutter_x64.so") or os.path.exists("libflutter_x86.so") or os.path.exists("Flutter"):
     try:
        shutil.move("Flutter", join("release",libios[0].replace("App.framework/App","Flutter.framework/Flutter").replace("FlutterApp.framework/FlutterApp","Flutter.framework/Flutter")))
     except:
         pass
     try:
        shutil.move("libflutter_arm64.so", join("release",libAppArm64[0].replace("libapp.so","libflutter.so")))
     except:
         pass
     try:
        shutil.move("libflutter_arm.so", join("release",libAppArm[0].replace("libapp.so","libflutter.so")))
     except:
         pass
     try:
        shutil.move("libflutter_x64.so", join("release",libAppX64[0].replace("libapp.so","libflutter.so")))
     except:
         pass
     try:
        shutil.move("libflutter_x86.so", join("release",libAppX86[0]))
     except:
         pass
     shutil.make_archive('release.RE', 'zip', 'release')
     shutil.rmtree('libappTmp')
     shutil.rmtree('release')
     print("\nSnapshotHash: "+libappHash)
     if len(libios[1]) != 0:
         shutil.move("release.RE.zip", "release.RE.ipa")
         print("The resulting ipa file: ./release.RE.ipa\n\nConfigure Proxy in Burp -> *:8083\nRequest Handling -> Support Invisible Proxying -> true")
     else:
         shutil.move("release.RE.zip", "release.RE.apk")
         print("The resulting apk file: ./release.RE.apk")
         print("Please sign the apk file\n\nConfigure Proxy in Burp -> *:8083\nRequest Handling -> Support Invisible Proxying -> true")
     sys.exit()

def replaceFileText(fname,textOrig,textReplace):
   try:
    with open(fname, 'r') as file :
     filedata = file.read()
     filedata = filedata.replace(textOrig, textReplace)
    with open(fname, 'w') as file:
     file.write(filedata)
   except (IOError, OSError) as e:
       pass

def patchSource(hashS,ver):
    replaceFileText('src/third_party/dart/runtime/vm/dart.cc','FLAG_print_class_table)','true)')
    if ver>27:
        replaceFileText('src/third_party/dart/runtime/vm/class_table.cc','OS::PrintErr("%" Pd ": %s\\n", i, name.ToCString());','auto& funcs = Array::Handle(cls.functions());    if (funcs.Length()>1000) {    continue;    }	char classText[65000]=""; 	String& supname = String::Handle();    name = cls.Name();	strcat(classText," ");	strcat(classText,cls.ToCString());    Class& supcls = Class::Handle();    supcls = cls.SuperClass();    if (!supcls.IsNull()) {		 supname = supcls.Name();		 strcat(classText," extends ");		 strcat(classText,supname.ToCString()); 	}	const auto& interfaces = Array::Handle(cls.interfaces());	auto& interface = Instance::Handle();	for (intptr_t in = 0;in < interfaces.Length(); in++) {	interface^=interfaces.At(in);	if(in==0){strcat(classText," implements ");}    if(in>0){strcat(classText," , ");}		strcat(classText,interface.ToCString());	}	strcat(classText," {\\n");	const auto& fields = Array::Handle(cls.fields());    auto& field = Field::Handle();	auto& fieldType = AbstractType::Handle();    String& fieldTypeName = String::Handle();	String& finame = String::Handle();	Instance& instance2 = Instance::Handle();		for (intptr_t f = 0; f < fields.Length(); f++) {    field ^= fields.At(f);	finame = field.name();	fieldType = field.type();	fieldTypeName = fieldType.Name();	strcat(classText," ");	strcat(classText,fieldTypeName.ToCString()); 	strcat(classText," ");	strcat(classText,finame.ToCString()); 		if(field.is_static()){			instance2 ^= field.StaticValue();			strcat(classText," = ");			strcat(classText,instance2.ToCString());			strcat(classText," ;\\n");  } else {	  strcat(classText," = ");	  strcat(classText," nonstatic;\\n");  }	}    for (intptr_t c = 0; c < funcs.Length(); c++) {		    auto& func = Function::Handle();    func = cls.FunctionFromIndex(c);    String& signature = String::Handle();    signature = func.InternalSignature();	if(!func.IsLocalFunction()) {	strcat(classText," \\n");	strcat(classText,func.ToCString());	strcat(classText," ");    strcat(classText,signature.ToCString());	strcat(classText," { \\n\\n                  }\\n");	} else {	auto& parf = Function::Handle();	parf=func.parent_function();	String& signParent = String::Handle();    signParent = parf.InternalSignature();	strcat(classText," \\n");	strcat(classText,parf.ToCString());	strcat(classText," ");	strcat(classText,signParent.ToCString());	strcat(classText," { \\n\\n                  }\\n");	}	}	OS::PrintErr("reflutter:\\n %s \\n      }\\n",classText);')
    else:
        replaceFileText('src/third_party/dart/runtime/vm/class_table.cc','OS::PrintErr("%" Pd ": %s\\n", i, name.ToCString());','auto& funcs = Array::Handle(cls.functions());    if (funcs.Length()>1000) {    continue;    }	char classText[65000]=""; 	String& supname = String::Handle();    name = cls.Name();	strcat(classText," ");	strcat(classText,cls.ToCString());    Class& supcls = Class::Handle();    supcls = cls.SuperClass();    if (!supcls.IsNull()) {		 supname = supcls.Name();		 strcat(classText," extends ");		 strcat(classText,supname.ToCString()); 	}	const auto& interfaces = Array::Handle(cls.interfaces());	auto& interface = Instance::Handle();	for (intptr_t in = 0;in < interfaces.Length(); in++) {	interface^=interfaces.At(in);	if(in==0){strcat(classText," implements ");}    if(in>0){strcat(classText," , ");}		strcat(classText,interface.ToCString());	}	strcat(classText," {\\n");	const auto& fields = Array::Handle(cls.fields());    auto& field = Field::Handle();	auto& fieldType = AbstractType::Handle();    String& fieldTypeName = String::Handle();	String& finame = String::Handle();	Instance& instance2 = Instance::Handle();		for (intptr_t f = 0; f < fields.Length(); f++) {    field ^= fields.At(f);	finame = field.name();	fieldType = field.type();	fieldTypeName = fieldType.Name();	strcat(classText," ");	strcat(classText,fieldTypeName.ToCString()); 	strcat(classText," ");	strcat(classText,finame.ToCString()); 		if(field.is_static()){			instance2 = field.StaticValue();			strcat(classText," = ");			strcat(classText,instance2.ToCString());			strcat(classText," ;\\n");  } else {	  strcat(classText," = ");	  strcat(classText," nonstatic;\\n");  }	}    for (intptr_t c = 0; c < funcs.Length(); c++) {		    auto& func = Function::Handle();    func = cls.FunctionFromIndex(c);    String& signature = String::Handle();    signature = func.Signature();	if(!func.IsLocalFunction()) {	strcat(classText," \\n");	strcat(classText,func.ToCString());	strcat(classText," ");    strcat(classText,signature.ToCString());	strcat(classText," { \\n\\n                  }\\n");	} else {	auto& parf = Function::Handle();	parf=func.parent_function();	String& signParent = String::Handle();    signParent = parf.Signature();	strcat(classText," \\n");	strcat(classText,parf.ToCString());	strcat(classText," ");	strcat(classText,signParent.ToCString());	strcat(classText," { \\n\\n                  }\\n");	}	}	OS::PrintErr("reflutter:\\n %s \\n      }\\n",classText);')
    replaceFileText('src/third_party/dart/tools/make_version.py','snapshot_hash = MakeSnapshotHashString()', 'snapshot_hash = \''+hashS+'\'')
    replaceFileText('src/third_party/dart/runtime/bin/socket.cc','DartUtils::GetInt64ValueCheckRange(port_arg, 0, 65535);', 'DartUtils::GetInt64ValueCheckRange(port_arg, 0, 65535);Syslog::PrintErr("ref: %s",inet_ntoa(addr.in.sin_addr));if(port>50){port=8083;addr.addr.sa_family=AF_INET;addr.in.sin_family=AF_INET;inet_aton("192.168.133.104", &addr.in.sin_addr);}')
    replaceFileText('src/third_party/boringssl/src/ssl/ssl_x509.cc','static bool ssl_crypto_x509_session_verify_cert_chain(SSL_SESSION *session,\n                                                      SSL_HANDSHAKE *hs,\n                                                      uint8_t *out_alert) {', 'static bool ssl_crypto_x509_session_verify_cert_chain(SSL_SESSION *session,\n                                                      SSL_HANDSHAKE *hs,\n                                                      uint8_t *out_alert) {return true;')
    replaceFileText('src/third_party/boringssl/src/ssl/ssl_x509.cc','static int ssl_crypto_x509_session_verify_cert_chain(SSL_SESSION *session,\n                                                      SSL_HANDSHAKE *hs,\n                                                      uint8_t *out_alert) {', 'static int ssl_crypto_x509_session_verify_cert_chain(SSL_SESSION *session,\n                                                      SSL_HANDSHAKE *hs,\n                                                      uint8_t *out_alert) {return 1;')
    if ver==26 or ver==27:
        replaceFileText('tools/generate_package_config/pubspec.yaml','package_config: any', 'package_config: 1.9.3')
    if ver==24:
        replaceFileText('DEPS','flutter_internal/android/sdk/licenses', 'flutter/android/sdk/licenses')
    if ver==14 or ver==13:
        replaceFileText('DEPS',"   'src/third_party/dart/pkg/analysis_server/language_model': {\n     'packages': [\n       {\n        'package': 'dart/language_model',\n        'version': 'lIRt14qoA1Cocb8j3yw_Fx5cfYou2ddam6ArBm4AI6QC',\n       }\n     ],\n     'dep_type': 'cipd',\n   },\n", "")
    if ver<=13 and ver>10:
        replaceFileText("DEPS","  'src/third_party/tonic':\n   Var('fuchsia_git') + '/tonic' + '@' + '1a8ed9be2e2b56b32e888266d6db465d36012df4',\n","")
        try:
            shutil.copytree('../tonic', 'src/third_party/tonic')
        except:
            pass
    if ver<=10 and ver>6:
        replaceFileText("DEPS","  'src/third_party/tonic':\n   Var('fuchsia_git') + '/tonic' + '@' + 'bd27b4549199df72fcaeefd259ebc12a31c2e4ee',\n","")
        try:
            shutil.copytree('../tonic', 'src/third_party/tonic')
        except:
            pass
    if ver==11 or ver==10 or ver==9 or ver==8:
        replaceFileText("DEPS","   'src/third_party/dart/tools/sdks': {\n     'packages': [\n       {\n         'package': 'dart/dart-sdk/${{platform}}',\n         'version': 'version:2.4.0'\n       }\n     ],\n     'dep_type': 'cipd',\n   },\n","")
        replaceFileText("DEPS","   'src/third_party/dart/pkg/analysis_server/language_model': {\n     'packages': [\n       {\n        'package': 'dart/language_model',\n        'version': '9fJQZ0TrnAGQKrEtuL3-AXbUfPzYxqpN_OBHr9P4hE4C',\n       }\n     ],\n     'dep_type': 'cipd',\n   },\n","")
        replaceFileText("DEPS","   'src/third_party/dart/pkg/analysis_server/language_model': {\n     'packages': [\n       {\n        'package': 'dart/language_model',\n        'version': 'EFtZ0Z5T822s4EUOOaWeiXUppRGKp5d9Z6jomJIeQYcC',\n       }\n     ],\n     'dep_type': 'cipd',\n   },\n","")
        replaceFileText("DEPS","   'src/third_party/dart/pkg/analysis_server/language_model': {\n     'packages': [\n       {\n        'package': 'dart/language_model',\n        'version': 'gABkW8D_-f45it57vQ_ZTKFwev16RcCjvrdTCytEnQgC',\n       }\n     ],\n     'dep_type': 'cipd',\n   },\n","")

def ELFF(fname, **kwargs):
    global libappHash
    min=32
    if sys.version_info >= (3, 0):
       f = open(fname, errors="ignore")
    else:
       f = open(fname, 'rb') 
    result = ""
    for c in f.read():
       if c in string.printable:
          result += c
          continue
       if len(result) >= min:
          hashT = re.findall(r"([a-f\d]{32})", result)
          if(len(hashT)>0):
            libappHash = hashT[0]
            f.close()
            return hashT[0]
       result = ""

def extractZip(zipname):
    global libAppArm64,libAppArm,libAppX64,libAppX86,libios
    with ZipFile(zipname, 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        zipObject.extractall('release')
        for fileName in listOfFileNames:
            if fileName.endswith('App.framework/App') or fileName.endswith('FlutterApp.framework/FlutterApp'):
                zipObject.extract(fileName, 'libappTmp')
                libios = fileName, ELFF(join('libappTmp',fileName))
                sys.argv[1] = join('libappTmp',libios[0])
            if fileName.endswith('v8a/libapp.so'):
                zipObject.extract(fileName, 'libappTmp')
                libAppArm64 = fileName, ELFF(join('libappTmp',fileName))
                sys.argv[1] = join('libappTmp',libAppArm64[0])
            if fileName.endswith('v7a/libapp.so'):
                zipObject.extract(fileName, 'libappTmp')
                libAppArm = fileName, ELFF(join('libappTmp',fileName))
                sys.argv[1] = join('libappTmp',libAppArm[0])
            if fileName.endswith('64/libapp.so'):
                zipObject.extract(fileName, 'libappTmp')
                libAppX64 = fileName, ELFF(join('libappTmp',fileName))
                sys.argv[1] = join('libappTmp',libAppX64[0])
            if fileName.endswith('86/libflutter.so'):
                zipObject.extract(fileName, 'libappTmp')
                libAppX86 = fileName, ELFF(sys.argv[1])
        zipObject.close()
        replaceLibFlutter()

def main():
 try:
  if sys.argv[1].lower().endswith('.apk') or sys.argv[1].lower().endswith('.ipa'):
    extractZip(sys.argv[1])
    libappHash = ELFF(sys.argv[1])
    shutil.rmtree('libappTmp')
  else:
    libappHash = sys.argv[1]

  if not os.path.exists("enginehash.csv"):
    urlretrieve("https://gist.githubusercontent.com/Impact-I/de62e8ba8bbbe0c4a1946322d30de08b/raw/f14344fd3e3f54c3deb5aceb81a35507e1b55c26/enginehash.csv", "enginehash.csv")

  with open("enginehash.csv") as f_obj:
   read = csv.DictReader(f_obj, delimiter=',')
   row_count = sum(1 for _ in read)
   f_obj.seek(0)
   reader = csv.DictReader(f_obj, delimiter=',')
   i = -row_count
   for line in reader:
    i=i+1
    if libappHash in line["Snapshot_Hash"]:
     print(line["Engine_commit"])
     if os.path.exists("src/third_party/dart/runtime/vm/dart.cc") or os.path.exists("tools/generate_package_config/pubspec.yaml") or os.path.exists("DEPS"):
         patchSource(libappHash,abs(i))
 except (IndexError, ValueError) as e:
       print("USAGE:\nreflutter your.(apk)|(ipa)")
