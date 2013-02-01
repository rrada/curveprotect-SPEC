Name:		curveprotect
Version:	20120918
Release:	1
Summary:	CurveProtect

Group:		Utilities/System
License:	Public Domain
URL:		http://curveprotect.org/
Source0:	curveprotect-20120918.tar.bz2

BuildRequires:	gcc
Requires:	daemontools, gnupg


%description
CurveProtect is set of tool which protect your network
communication.


%prep
%setup -q


%build
./do
# XXX: fix this
%define cphomedir "/opt/curveprotect"


%install
./do install %{buildroot}


%post
if [ ! -e /service ]; then
  if [ -e /etc/service ]; then
    ln -s /etc/service /service
  fi
fi

(
  (
    echo "IPADDR_START=127.10.10.10"
    echo "IPADDR_END=127.10.10.15"
    echo "NETMASK=255.0.0.0"
    echo "CLONENUM_START=0"
  ) > /etc/sysconfig/network-scripts/ifcfg-lo-range0.tmp
  mv -f /etc/sysconfig/network-scripts/ifcfg-lo-range0.tmp /etc/sysconfig/network-scripts/ifcfg-lo-range0
)

#copy scripts to sbin
for f in _postinst _postrm _prerm _removegroup _removeuser _createuser _creategroup; do
  cp -p %{cphomedir}"/bin/${f}" %{cphomedir}"/sbin/"
done

%{cphomedir}"/sbin/_postinst"


%preun
%{cphomedir}"/sbin/_prerm"


%postun
rm -f /etc/sysconfig/network-scripts/ifcfg-lo-range
%{cphomedir}"/sbin/_postrm"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, -, -, 0755)
/opt/curveprotect/bin/_creategroup
/opt/curveprotect/bin/_createuser
/opt/curveprotect/bin/_postinst
/opt/curveprotect/bin/_postrm
/opt/curveprotect/bin/_prerm
/opt/curveprotect/bin/_removegroup
/opt/curveprotect/bin/_removeuser
/opt/curveprotect/bin/addcr
/opt/curveprotect/bin/axfr-get
/opt/curveprotect/bin/axfrdns
/opt/curveprotect/bin/bindparser
/opt/curveprotect/bin/cpforwarder-conf
/opt/curveprotect/bin/cpprintkey32
/opt/curveprotect/bin/cpssh-conf
/opt/curveprotect/bin/cptelnet
/opt/curveprotect/bin/cpvpn-conf
/opt/curveprotect/bin/cpwrapper
/opt/curveprotect/bin/crxmake
/opt/curveprotect/bin/curvecpclient
/opt/curveprotect/bin/curvecpmakekey
/opt/curveprotect/bin/curvecpmessage
/opt/curveprotect/bin/curvecpprintkey
/opt/curveprotect/bin/curvecpserver
/opt/curveprotect/bin/delcr
/opt/curveprotect/bin/dnsaccess
/opt/curveprotect/bin/dnscache
/opt/curveprotect/bin/dnsfilter
/opt/curveprotect/bin/dnsip
/opt/curveprotect/bin/dnsipq
/opt/curveprotect/bin/dnsmx
/opt/curveprotect/bin/dnsname
/opt/curveprotect/bin/dnsq
/opt/curveprotect/bin/dnsqr
/opt/curveprotect/bin/dnstrace
/opt/curveprotect/bin/dnstracesort
/opt/curveprotect/bin/dnstxt
/opt/curveprotect/bin/dnsuser
/opt/curveprotect/bin/dnszonecleanup
/opt/curveprotect/bin/dnszonedata
/opt/curveprotect/bin/dnszonedownload
/opt/curveprotect/bin/dnszonefilter
/opt/curveprotect/bin/dnszonesign
/opt/curveprotect/bin/ed25519makekey
/opt/curveprotect/bin/ed25519printkey
/opt/curveprotect/bin/ed25519sign
/opt/curveprotect/bin/ed25519signopen
/opt/curveprotect/bin/envdir
/opt/curveprotect/bin/envuidgid
/opt/curveprotect/bin/extremeenvuidgid
/opt/curveprotect/bin/extremesetuidgid
/opt/curveprotect/bin/fdcopy
/opt/curveprotect/bin/fghack
/opt/curveprotect/bin/fixcrio
/opt/curveprotect/bin/fixservice
/opt/curveprotect/bin/forwarder-addservice
/opt/curveprotect/bin/forwarder-emptyservices
/opt/curveprotect/bin/forwarder-removeservice
/opt/curveprotect/bin/hextobase32
/opt/curveprotect/bin/http-get
/opt/curveprotect/bin/httpd
/opt/curveprotect/bin/httpproxy
/opt/curveprotect/bin/httpproxyconn
/opt/curveprotect/bin/jabberproxy
/opt/curveprotect/bin/killafter
/opt/curveprotect/bin/multilog
/opt/curveprotect/bin/nacl-sha256
/opt/curveprotect/bin/nacl-sha512
/opt/curveprotect/bin/netclient
/opt/curveprotect/bin/netcurvecpclient
/opt/curveprotect/bin/netcurvecpmessage
/opt/curveprotect/bin/nettcpclient
/opt/curveprotect/bin/nettunnel
/opt/curveprotect/bin/okabi
/opt/curveprotect/bin/okar-x86
/opt/curveprotect/bin/okc-x86
/opt/curveprotect/bin/okcpp-x86
/opt/curveprotect/bin/oklibs-x86
/opt/curveprotect/bin/pgrphack
/opt/curveprotect/bin/pkaccess
/opt/curveprotect/bin/pkaccess-data
/opt/curveprotect/bin/printenviron
/opt/curveprotect/bin/randomtext
/opt/curveprotect/bin/recordio
/opt/curveprotect/bin/setlock
/opt/curveprotect/bin/setuidgid
/opt/curveprotect/bin/shuffleargs
/opt/curveprotect/bin/sigpg
/opt/curveprotect/bin/softlimit
/opt/curveprotect/bin/svc
/opt/curveprotect/bin/svok
/opt/curveprotect/bin/svstat
/opt/curveprotect/bin/tai64n
/opt/curveprotect/bin/tai64nlocal
/opt/curveprotect/bin/tcpcat
/opt/curveprotect/bin/tcpclient
/opt/curveprotect/bin/tcprules
/opt/curveprotect/bin/tcprulescheck
/opt/curveprotect/bin/tcpserver
/opt/curveprotect/bin/tinydns
/opt/curveprotect/bin/tinydns-data
/opt/curveprotect/bin/tinydns-edit
/opt/curveprotect/bin/tinydns-get
/opt/curveprotect/bin/trycreatesupervise
/opt/curveprotect/bin/uidgidchown
/opt/curveprotect/bin/vpn
/opt/curveprotect/bin/vpn-addservice
/opt/curveprotect/bin/vpn-data
/opt/curveprotect/bin/vpn-emptyservices
/opt/curveprotect/bin/vpn-removeservice
/opt/curveprotect/etc/dnscache/env/CACHESIZE
/opt/curveprotect/etc/dnscache/env/DATALIMIT
/opt/curveprotect/etc/dnscache/env/IP
/opt/curveprotect/etc/dnscache/env/IPSEND
/opt/curveprotect/etc/dnscache/env/ROOT
/opt/curveprotect/etc/dnscache/root/ip/127
/opt/curveprotect/etc/dnscache/root/servers/@
/opt/curveprotect/etc/dnscache/root/servers/arpa
/opt/curveprotect/etc/dnscache/root/dump/
/opt/curveprotect/etc/dnslocal/conf/.rygplfawtlapigzsgdy
/opt/curveprotect/etc/dnslocal/conf/@/lock
/opt/curveprotect/etc/dnslocal/conf/@/period
/opt/curveprotect/etc/dnslocal/conf/@/run
/opt/curveprotect/etc/dnslocal/conf/arpa/lock
/opt/curveprotect/etc/dnslocal/conf/arpa/period
/opt/curveprotect/etc/dnslocal/conf/arpa/run
/opt/curveprotect/etc/dnslocal/conf/lock
/opt/curveprotect/etc/dnslocal/env/CFGDIR
/opt/curveprotect/etc/dnslocal/env/DNSCACHEIP
/opt/curveprotect/etc/dnslocal/env/EMPTYDIRECTORY
/opt/curveprotect/etc/dnslocal/env/FAKETTL
/opt/curveprotect/etc/dnslocal/env/IP
/opt/curveprotect/etc/dnslocal/env/MAKECDB
/opt/curveprotect/etc/dnslocal/env/REMOVELOC
/opt/curveprotect/etc/dnslocal/env/ROOT
/opt/curveprotect/etc/dnslocal/env/VARDIR
/opt/curveprotect/etc/httpd/env/IP
/opt/curveprotect/etc/httpd/env/PORT
/opt/curveprotect/etc/httpd/env/PYTHONPATH
/opt/curveprotect/etc/httpd/env/ROOT
/opt/curveprotect/etc/httpd/env/TMPDIR
/opt/curveprotect/etc/httpd/env/WWWDIR
/opt/curveprotect/etc/httpproxy/env/ALLOWUNENCRYPTED
/opt/curveprotect/etc/httpproxy/env/DNSCACHEIP
/opt/curveprotect/etc/httpproxy/env/IP
/opt/curveprotect/etc/httpproxy/env/PORT
/opt/curveprotect/etc/httpproxy/env/ROOT
/opt/curveprotect/etc/httpproxy/env/SIGPG_SLEEP
/opt/curveprotect/etc/httpproxy/env/TIMEOUT
/opt/curveprotect/etc/jabberproxy/env/DNSCACHEIP
/opt/curveprotect/etc/jabberproxy/env/IP
/opt/curveprotect/etc/jabberproxy/env/PORT
/opt/curveprotect/etc/jabberproxy/env/ROOT
/opt/curveprotect/etc/jabberproxy/env/TIMEOUT
/opt/curveprotect/etc/tmp/
/opt/curveprotect/html/_colors.css
/opt/curveprotect/html/_dns.css
/opt/curveprotect/html/_footer.html
/opt/curveprotect/html/_forwarder.css
/opt/curveprotect/html/_global.css
/opt/curveprotect/html/_header.html
/opt/curveprotect/html/_keys.css
/opt/curveprotect/html/_proxy.css
/opt/curveprotect/html/_stats.css
/opt/curveprotect/html/_troubleshooting.css
/opt/curveprotect/html/_vpn.css
/opt/curveprotect/html/data.html
/opt/curveprotect/html/dns.html
/opt/curveprotect/html/dns_stats.html
/opt/curveprotect/html/ed25519keys.html
/opt/curveprotect/html/forwarder.html
/opt/curveprotect/html/httpproxy_stats.html
/opt/curveprotect/html/index.html
/opt/curveprotect/html/keys.html
/opt/curveprotect/html/log.html
/opt/curveprotect/html/proxy.html
/opt/curveprotect/html/troubleshooting.html
/opt/curveprotect/html/vpn.html
/opt/curveprotect/lib/base32.py
/opt/curveprotect/lib/base32.pyc
/opt/curveprotect/lib/base32.pyo
/opt/curveprotect/lib/check.py
/opt/curveprotect/lib/check.pyc
/opt/curveprotect/lib/check.pyo
/opt/curveprotect/lib/config.py
/opt/curveprotect/lib/config.pyc
/opt/curveprotect/lib/config.pyo
/opt/curveprotect/lib/curvecp.py
/opt/curveprotect/lib/curvecp.pyc
/opt/curveprotect/lib/curvecp.pyo
/opt/curveprotect/lib/dns.py
/opt/curveprotect/lib/dns.pyc
/opt/curveprotect/lib/dns.pyo
/opt/curveprotect/lib/ed25519.py
/opt/curveprotect/lib/ed25519.pyc
/opt/curveprotect/lib/ed25519.pyo
/opt/curveprotect/lib/footer.py
/opt/curveprotect/lib/footer.pyc
/opt/curveprotect/lib/footer.pyo
/opt/curveprotect/lib/header.py
/opt/curveprotect/lib/header.pyc
/opt/curveprotect/lib/header.pyo
/opt/curveprotect/lib/htmltemplate.py
/opt/curveprotect/lib/htmltemplate.pyc
/opt/curveprotect/lib/htmltemplate.pyo
/opt/curveprotect/lib/lib.py
/opt/curveprotect/lib/lib.pyc
/opt/curveprotect/lib/lib.pyo
/opt/curveprotect/lib/slownacl/__init__.py
/opt/curveprotect/lib/slownacl/__init__.pyc
/opt/curveprotect/lib/slownacl/__init__.pyo
/opt/curveprotect/lib/slownacl/curve25519.py
/opt/curveprotect/lib/slownacl/curve25519.pyc
/opt/curveprotect/lib/slownacl/curve25519.pyo
/opt/curveprotect/lib/slownacl/poly1305.py
/opt/curveprotect/lib/slownacl/poly1305.pyc
/opt/curveprotect/lib/slownacl/poly1305.pyo
/opt/curveprotect/lib/slownacl/salsa20.py
/opt/curveprotect/lib/slownacl/salsa20.pyc
/opt/curveprotect/lib/slownacl/salsa20.pyo
/opt/curveprotect/lib/slownacl/salsa20hmacsha512.py
/opt/curveprotect/lib/slownacl/salsa20hmacsha512.pyc
/opt/curveprotect/lib/slownacl/salsa20hmacsha512.pyo
/opt/curveprotect/lib/slownacl/sha512.py
/opt/curveprotect/lib/slownacl/sha512.pyc
/opt/curveprotect/lib/slownacl/sha512.pyo
/opt/curveprotect/lib/slownacl/test.py
/opt/curveprotect/lib/slownacl/test.pyc
/opt/curveprotect/lib/slownacl/test.pyo
/opt/curveprotect/lib/slownacl/util.py
/opt/curveprotect/lib/slownacl/util.pyc
/opt/curveprotect/lib/slownacl/util.pyo
/opt/curveprotect/lib/slownacl/verify.py
/opt/curveprotect/lib/slownacl/verify.pyc
/opt/curveprotect/lib/slownacl/verify.pyo
/opt/curveprotect/lib/slownacl/xsalsa20poly1305.py
/opt/curveprotect/lib/slownacl/xsalsa20poly1305.pyc
/opt/curveprotect/lib/slownacl/xsalsa20poly1305.pyo
/opt/curveprotect/lib/tcpping.py
/opt/curveprotect/lib/tcpping.pyc
/opt/curveprotect/lib/tcpping.pyo
/opt/curveprotect/log/addremoveservice
/opt/curveprotect/log/dnscache
/opt/curveprotect/log/dnslocal
/opt/curveprotect/log/dnslocaldownload
/opt/curveprotect/log/dnslocaltcp
/opt/curveprotect/log/httpd
/opt/curveprotect/log/httpproxy
/opt/curveprotect/log/jabberproxy
/opt/curveprotect/sbin/
/opt/curveprotect/service/addremoveservice/log/run
/opt/curveprotect/service/addremoveservice/run
/opt/curveprotect/service/dnscache/log/run
/opt/curveprotect/service/dnscache/run
/opt/curveprotect/service/dnslocal/log/run
/opt/curveprotect/service/dnslocal/run
/opt/curveprotect/service/dnslocaldownload/log/run
/opt/curveprotect/service/dnslocaldownload/run
/opt/curveprotect/service/dnslocaltcp/log/run
/opt/curveprotect/service/dnslocaltcp/run
/opt/curveprotect/service/httpd/log/run
/opt/curveprotect/service/httpd/run
/opt/curveprotect/service/httpproxy/log/run
/opt/curveprotect/service/httpproxy/run
/opt/curveprotect/service/jabberproxy/log/run
/opt/curveprotect/service/jabberproxy/run
/opt/curveprotect/share/chrome/background.js
/opt/curveprotect/share/chrome/defaults.js
/opt/curveprotect/share/chrome/icon-128.png
/opt/curveprotect/share/chrome/icon-black.png
/opt/curveprotect/share/chrome/icon-green.png
/opt/curveprotect/share/chrome/icon-red.png
/opt/curveprotect/share/chrome/icon-yellow.png
/opt/curveprotect/share/chrome/manifest.json
/opt/curveprotect/share/chrome/options.html
/opt/curveprotect/share/curveprotect-20120918.crx
/opt/curveprotect/share/curveprotect-20120918.zip
/opt/curveprotect/share/gnupgkey-20E3C425-valid-to-20130206.pub
/opt/curveprotect/share/nacl-20110221-data.gz
/opt/curveprotect/share/nacl-20110221-log.gz
/opt/curveprotect/var/dnslocal/.rygplfawtlapigzsgdy
/opt/curveprotect/var/dnslocal/root/lock
/opt/curveprotect/var/dnslocal/tmp/
/opt/curveprotect/var/dnslocal/tmp1/
/opt/curveprotect/var/dnslocal/tmp2/
/opt/curveprotect/var/dnslocal/tmp3/
/opt/curveprotect/var/dnslocal/zones/
/opt/curveprotect/var/dnslocal/zonessigned/
/opt/curveprotect/var/dnslocal/out/
/opt/curveprotect/var/dnslocal/empty/
/opt/curveprotect/var/lock
/opt/curveprotect/tmp/
/opt/curveprotect/www/curvecpkeys.dynhtml
/opt/curveprotect/www/data.dynhtml
/opt/curveprotect/www/dns.dynhtml
/opt/curveprotect/www/dns_dnscacheconfig.dynhtml
/opt/curveprotect/www/dns_dnslocalconfig.dynhtml
/opt/curveprotect/www/dns_dnsrootconfig.dynhtml
/opt/curveprotect/www/dns_stats.dynhtml
/opt/curveprotect/www/dnscurvekeys.dynhtml
/opt/curveprotect/www/ed25519keys.dynhtml
/opt/curveprotect/www/ed25519keys_config.dynhtml
/opt/curveprotect/www/forwarder.dynhtml
/opt/curveprotect/www/forwarder_config.dynhtml
/opt/curveprotect/www/httpproxy_stats.dynhtml
/opt/curveprotect/www/index.dynhtml
/opt/curveprotect/www/keys_config.dynhtml
/opt/curveprotect/www/log.dynhtml
/opt/curveprotect/www/proxy.dynhtml
/opt/curveprotect/www/proxy_config.dynhtml
/opt/curveprotect/www/static/curveprotect-logo.png
/opt/curveprotect/www/troubleshooting.dynhtml
/opt/curveprotect/www/vpn.dynhtml
/opt/curveprotect/www/vpn_aclconfig.dynhtml
/opt/curveprotect/www/vpn_config.dynhtml


%doc README

%changelog
* Tue Nov 06 2012 - radek.rada (at) gmail.com
- Initial implementation
