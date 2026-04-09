.. _goui:


GroupOffice User Interface Framework
=====================================

Introducing GOUI
----------------

Since version 6.7, we have started phasing out ExtJS in favor of our own TypeScript framework.
We have named it GOUI, which is short for GroupOffice User Interface. As of 2023, ExtJS is considered obsolete
and it contains unnecessary compatibility layers for browsers that have been obsoleted for years now. As yet,
GroupOffice will keep supporting ExtJS, but all new development will use the GOUI framework.

GOUI is written in `TypeScript <https://typescriptlang.org>` and is intended to generate clean Javascript and HTML code.
In that respect, GOUI is clearly inspired by ExtJS. However, the generated code is more suited to more modern standards
for Javascript, HTML and CSS. Also, since we compile our code into modern Javascript, it will be more secure by default.


GOUI Documentation
-------------------

You can find the full documentation on our `GOUI documentation site <https://goui.io>`_.

GroupOffice library for GOUI
-----------------------------

To get ahead of the rewrite of the :ref:`web client tutorial <webclient_module>`, please note that in order to start
developing modules in GOUI, you need the GOUI-Groupoffice package as well. If you use our Docker Development environment,
it will be installed automatically as long as you develop against 6.7 or up.
