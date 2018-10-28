<%inherit file="_base.mako"/>
<% import datetime %>

Hello, World!
${datetime.datetime.now() | h}
