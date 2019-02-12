Best practice
=============

Structure
---------

We are in transation from an old to a new API. Old code use captial letters "GO.*" namespaces. New code uses small letters "go.*".

The new API can be found in the following folders:

- go/modules/<package>/<module>/views/extjs3/*
- go/core/views/extjs3/*


Extending
=========

When extending components with Ext.extend() always override initComponent and not the constructor::

  go.modules.pkg.mymodule.MyComp = Ext.extend(Ext.Panel, {
    initComponent: function() {
      go.modules.pkg.mymodule.MyComp.superclass.initComponent.call(this);

      //Do your initialization here
    }
  });
  
  
Core overrides are put in views/Extjs3/javascript/overrides.js
