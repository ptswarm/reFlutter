![workflow](https://github.com/ptswarm/reFlutter/actions/workflows/main.yml/badge.svg)

![stars](https://img.shields.io/github/stars/ptswarm/reFlutter)
[![github_downloads](https://img.shields.io/github/downloads/ptswarm/reFlutter/total?label=downloads&logo=github)](https://github.com/Impact-I/x8-Burp/releases/tag/)
<h3 align="center">reFlutter</h3>

#

<p align="center"><img src="https://user-images.githubusercontent.com/87244850/135372439-822467e7-03db-4593-9063-09a2cec460c2.jpg" width="100%"/></p>


Reverse Flutter


## Install
```
pip install reflutter

pip3 install reflutter
```
## Usage
```console
impact@f:~$ reflutter main.apk

Please enter your Burp IP: <input_ip>

SnapshotHash: 8ee4ef7a67df9845fba331734198a953
The resulting apk file: ./release.RE.apk
Please sign the apk file

Configure Proxy in Burp -> *:8083
Request Handling -> Support Invisible Proxying -> true

impact@f:~$ reflutter main.ipa
```
