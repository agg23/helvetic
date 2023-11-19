# helvetic

*helvetic* is an application that replaces the web service for the FitBit Aria.

The software is a work-in-progress, and runs as a Django application.  It also includes a bare-bones implementation of the protocol for testing, which uses bottle.py (and stores no data).

It requires local DNS spoofing in order to intercept requests originally bound for `fitbit.com`.

## Currently implemented

* Recording data
* Sending preferences and 1-2 user profiles to Aria
* Registering new device

## Partially implemented

* Viewing data (through Django Admin)
* Configuration manager (through Django Admin)
* Profile manager (through Django Admin)
* Sending more than 1 user profile to Aria

## Planned

* WiFi connection setup & complete registration flow
* Replacing bits that depend on Django Admin
* User management
* Data access
* Graphs

## Setup

**TODO:** Finish

```bash
python manage.py migrate
python manage.py createsuperuser --username=foo --email=foo@example.com
```

Set up DNS forwarding from `fitbit.com` to your Docker container.

**NOTE:** You must bind this container to port 80 on the host, otherwise the DNS redirect will not work.

## See also

* `protocol.md` - Contains information about the FitBit Aria protocol (version 3)
* `firmware.md` - Notes on the firmware
* `gfit.md` - Plans/notes on implementing [Google Fit](https://fit.google.com) support

