# These and other macros are documented in dhd/droid-hal-device.inc
%define device armani
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 1S
%define installable_zip 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
