# incy-ru-bypass

Auto-updating [Incy](https://docs.incy.cc) routing profile: traffic to domains/IPs
blocked or commonly needed-proxied in Russia goes through the VPN, everything else
goes direct.

Rebuilt every 12 hours by GitHub Actions from
[1andrevich/Re-filter-lists](https://github.com/1andrevich/Re-filter-lists)
(`community.lst` / `community_ips.lst`).

Add to Incy via autorouting, pointing at:

```
https://raw.githubusercontent.com/khizrim/incy-ru-bypass/main/ru-bypass.json
```
