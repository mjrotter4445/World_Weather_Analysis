<!DOCTYPE html>
<!-- saved from url=(0040)https://home.openweathermap.org/api_keys -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script type="text/javascript" src="./api_files/2391b64adb"></script><script type="text/javascript" async="" src="./api_files/analytics.js.download"></script><script src="./api_files/nr-1209.min.js.download"></script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam-cell.nr-data.net","errorBeacon":"bam-cell.nr-data.net","licenseKey":"2391b64adb","applicationID":"8943572","transactionName":"cwwNRUNWXw5QFk1VRlk8CFRIShwLWwAHTA==","queueTime":0,"applicationTime":18,"agent":""}</script>
<script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"2391b64adb",applicationID:"8943572"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var i=e[n]={exports:{}};t[n][0].call(i.exports,function(e){var i=t[n][1][e];return r(i||e)},i,i.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(t,e,n){function r(){}function i(t,e,n){return function(){return o(t,[u.now()].concat(f(arguments)),e?null:this,n),e?void 0:this}}var o=t("handle"),a=t(8),f=t(9),c=t("ee").get("tracer"),u=t("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(t,e){s[e]=i(p+e,!0,"api")}),s.addPageAction=i(p+"addPageAction",!0),s.setCurrentRouteName=i(p+"routeName",!0),e.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(t,e){var n={},r=this,i="function"==typeof e;return o(l+"tracer",[u.now(),t,n],r),function(){if(c.emit((i?"":"no-")+"fn-start",[u.now(),r,i],n),i)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[u.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){m[e]=i(l+e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),o("err",[t,u.now(),!1,e])}},{}],2:[function(t,e,n){function r(t){if(NREUM.init){for(var e=NREUM.init,n=t.split("."),r=0;r<n.length-1;r++)if(e=e[n[r]],"object"!=typeof e)return;return e=e[n[n.length-1]]}}e.exports={getConfiguration:r}},{}],3:[function(t,e,n){function r(){return f.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,f=t(10);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=i},{}],4:[function(t,e,n){function r(t){return!(!t||!t.protocol||"file:"===t.protocol)}e.exports=r},{}],5:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?d("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&d("timing",["fcp",Math.floor(t.startTime)])})}function i(t,e){var n=t.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function o(t){t.getEntries().forEach(function(t){t.hadRecentInput||d("cls",[t])})}function a(t){if(t instanceof m&&!g){var e=Math.round(t.timeStamp),n={type:t.type};e<=p.now()?n.fid=p.now()-e:e>p.offset&&e<=Date.now()?(e-=p.offset,n.fid=p.now()-e):e=p.now(),g=!0,d("timing",["fi",e,n])}}function f(t){d("pageHide",[p.now(),t])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var c,u,s,d=t("handle"),p=t("loader"),l=t(7),m=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){c=new PerformanceObserver(r);try{c.observe({entryTypes:["paint"]})}catch(v){}u=new PerformanceObserver(i);try{u.observe({entryTypes:["largest-contentful-paint"]})}catch(v){}s=new PerformanceObserver(o);try{s.observe({type:"layout-shift",buffered:!0})}catch(v){}}if("addEventListener"in document){var g=!1,h=["click","keydown","mousedown","pointerdown","touchstart"];h.forEach(function(t){document.addEventListener(t,a,!1)})}l(f)}},{}],6:[function(t,e,n){function r(t,e){if(!i)return!1;if(t!==i)return!1;if(!e)return!0;if(!o)return!1;for(var n=o.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var f=navigator.userAgent,c=f.match(a);c&&f.indexOf("Chrome")===-1&&f.indexOf("Chromium")===-1&&(i="Safari",o=c[1])}e.exports={agent:i,version:o,match:r}},{}],7:[function(t,e,n){function r(t){function e(){t(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,e,!1)}e.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],8:[function(t,e,n){function r(t,e){var n=[],r="",o=0;for(r in t)i.call(t,r)&&(n[o]=e(r,t[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],9:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,i=n-e||0,o=Array(i<0?0:i);++r<i;)o[r]=t[e+r];return o}e.exports=r},{}],10:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function i(t){function e(t){return t&&t instanceof r?t:t?u(t,c,a):a()}function n(n,r,i,o,a){if(a!==!1&&(a=!0),!l.aborted||o){t&&a&&t(n,r,i);for(var f=e(i),c=v(n),u=c.length,s=0;s<u;s++)c[s].apply(f,r);var p=d[w[n]];return p&&p.push([b,n,r,f]),f}}function o(t,e){y[t]=v(t).concat(e)}function m(t,e){var n=y[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function v(t){return y[t]||[]}function g(t){return p[t]=p[t]||i(n)}function h(t,e){l.aborted||s(t,function(t,n){e=e||"feature",w[n]=e,e in d||(d[e]=[])})}var y={},w={},b={on:o,addEventListener:o,removeEventListener:m,emit:n,get:g,listeners:v,context:e,buffer:h,abort:f,aborted:!1};return b}function o(t){return u(t,c,a)}function a(){return new r}function f(){(d.api||d.feature)&&(l.aborted=!0,d=l.backlog={})}var c="nr@context",u=t("gos"),s=t(8),d={},p={},l=e.exports=i();e.exports.getOrSetContext=o,l.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(i.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return t[e]=r,r}var i=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){i.buffer([t],r),i.emit(t,e,n)}var i=t("ee").get("handle");e.exports=r,r.ee=i},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,o,function(){return i++})}var i=1,o="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!R++){var t=M.info=NREUM.info,e=v.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return u.abort();c(E,function(e,n){t[e]||(t[e]=n)});var n=a();f("mark",["onload",n+M.offset],null,"api"),f("timing",["load",n]);var r=v.createElement("script");0===t.agent.indexOf("http://")||0===t.agent.indexOf("https://")?r.src=t.agent:r.src=l+"://"+t.agent,e.parentNode.insertBefore(r,e)}}function i(){"complete"===v.readyState&&o()}function o(){f("mark",["domContent",a()+M.offset],null,"api")}var a=t(3),f=t("handle"),c=t(8),u=t("ee"),s=t(6),d=t(4),p=t(2),l=p.getConfiguration("ssl")===!1?"http":"https",m=window,v=m.document,g="addEventListener",h="attachEvent",y=m.XMLHttpRequest,w=y&&y.prototype,b=!d(m.location);NREUM.o={ST:setTimeout,SI:m.setImmediate,CT:clearTimeout,XHR:y,REQ:m.Request,EV:m.Event,PR:m.Promise,MO:m.MutationObserver};var x=""+location,E={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1209.min.js"},O=y&&w&&w[g]&&!/CriOS/.test(navigator.userAgent),M=e.exports={offset:a.getLastTimestamp(),now:a,origin:x,features:{},xhrWrappable:O,userAgent:s,disabled:b};if(!b){t(1),t(5),v[g]?(v[g]("DOMContentLoaded",o,!1),m[g]("load",r,!1)):(v[h]("onreadystatechange",i),m[h]("onload",r)),f("mark",["firstbyte",a.getLastTimestamp()],null,"api");var R=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,c,u){function nrWrapper(){var o,a,s,p;try{a=this,o=d(arguments),s="function"==typeof r?r(o,a):r||{}}catch(l){i([l,"",[o,a,c],s],t)}f(n+"start",[o,a,c],s,u);try{return p=e.apply(a,o)}catch(m){throw f(n+"err",[o,a,m],s,u),m}finally{f(n+"end",[o,a,p],s,u)}}return a(e)?e:(n||(n=""),nrWrapper[p]=e,o(e,nrWrapper,t),nrWrapper)}function r(t,e,r,i,o){r||(r="");var f,c,u,s="-"===r.charAt(0);for(u=0;u<e.length;u++)c=e[u],f=t[c],a(f)||(t[c]=n(f,s?c+r:r,i,c,o))}function f(n,r,o,a){if(!m||e){var f=m;m=!0;try{t.emit(n,r,o,e,a)}catch(c){i([c,n,r,o],t)}m=f}}return t||(t=s),n.inPlace=r,n.flag=p,n}function i(t,e){e||(e=s);try{e.emit("internal-error",t)}catch(n){}}function o(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(o){i([o],n)}for(var a in t)l.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[p])}function f(t,e){var n=e(t);return n[p]=t,o(t,n,s),n}function c(t,e,n){var r=t[e];t[e]=f(r,n)}function u(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var s=t("ee"),d=t(9),p="nr@original",l=Object.prototype.hasOwnProperty,m=!1;e.exports=r,e.exports.wrapFunction=f,e.exports.wrapInPlace=c,e.exports.argsToArray=u},{}]},{},["loader"]);</script>
<title>Members</title>
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<link rel="stylesheet" media="screen" href="./api_files/application-5c1ac6948f8598164f1fcbf2013c244a5915197f44305e3504dff1ed5f3eab23.css">
<link rel="stylesheet" media="screen" href="./api_files/css">
<link rel="stylesheet" media="screen" href="./api_files/css(1)">
<link rel="shortcut icon" type="image/x-icon" href="https://home.openweathermap.org/assets/logo_60x60-f0d7be5dcdc85ad03a401b5ab9e218c24b42dfcf45a01bec7b69a0a74ea7e5e6.png">
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="TqIgc0q/Dh0VuFrgLjB9qkA1DprdiJAlS6hlGk3XUsxN7C+Xl2BxwxR89iAoT7uv/zCtbKfeZegNYxTyXAZjig==">
</head>
<body class="body-orange" onclick="closeDropdowns(event)">
<nav id="nav-website" onclick="toggleMenu(event)">
<ul id="first-level-nav">
<li class="logo">
<a href="https://openweathermap.org/"><img src="./api_files/logo_white-011958e697955be95bdc4af6a4d1913dbf9df990cb9101a67c439879293f5947.png" alt="Logo white">
</a></li>
<li id="hamburger">
<img src="./api_files/icon_hamburger-6d9b3ca94227715d1be7bf5950e97e5acad3a84b0e604db61cce1f5aa0d529ef.svg" alt="Icon hamburger">
</li>
<div id="desktop-menu">
<form action="https://openweathermap.org/find" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓">
<input name="q" placeholder="Weather in your city" type="text">
<input style="display:none;" type="submit">
</form>

<ul class="desktop">
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;guide&#39;]);" href="https://openweathermap.org/guide">Guide</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;api&#39;]);" href="https://openweathermap.org/api">API</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/price">Pricing</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/weathermap">Maps</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/our-initiatives">Our Initiatives</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;examples&#39;]);" href="https://openweathermap.org/examples">Partners</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;news&#39;]);" target="_blank" href="https://openweather.co.uk/blog/category/weather">Blog</a>
</li>
<li>
<a class="marketplace" onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;marketplace&#39;]);" href="https://home.openweathermap.org/marketplace">Marketplace</a>
</li>
<li class="with-dropdown user-li">
<div id="user-dropdown">
<div class="inner-user-container">
mjrotter
</div>
</div>
<ul class="dropdown-menu" id="user-dropdown-menu">
<li>
<a href="https://home.openweathermap.org/myservices">My services</a>
</li>
<li>
<a href="https://home.openweathermap.org/api_keys">My API keys</a>
</li>
<li>
<a href="https://home.openweathermap.org/payments">My payments</a>
</li>
<li>
<a href="https://home.openweathermap.org/home">My profile</a>
</li>
<li>
<a class="logout" rel="nofollow" data-method="delete" href="https://home.openweathermap.org/users/sign_out">Logout
</a></li>
</ul>
</li>
<li class="with-dropdown">
<div id="support-dropdown">
Support
</div>
<ul class="dropdown-menu" id="support-dropdown-menu">
<li>
<a href="https://openweathermap.org/faq">FAQ</a>
</li>
<li>
<a href="https://openweathermap.org/appid">How to start</a>
</li>
<li>
<a href="https://home.openweathermap.org/questions">Ask a question</a>
</li>
</ul>
</li>
</ul>
</div>
</ul>
<ul id="mobile-menu">
<li>
<form action="https://openweathermap.org/find" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓">
<input name="q" placeholder="Weather in your city" type="text">
<input style="display:none;" type="submit">
</form>

</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;guide&#39;]);" href="https://openweathermap.org/guide">Guide</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;api&#39;]);" href="https://openweathermap.org/api">API</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/price">Pricing</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/weathermap">Maps</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;price&#39;]);" href="https://openweathermap.org/our-initiatives">Our Initiatives</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;examples&#39;]);" href="https://openweathermap.org/examples">Partners</a>
</li>
<li>
<a onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;news&#39;]);" target="_blank" href="https://openweather.co.uk/blog/category/weather">Blog</a>
</li>
<li>
<a href="https://home.openweathermap.org/questions">Ask a question</a>
</li>
<li>
<a class="marketplace" onclick="_gaq.push([&#39;_trackEvent&#39;, &#39;Navbar&#39;, &#39;Main&#39;, &#39;marketplace&#39;]);" href="https://home.openweathermap.org/marketplace">Marketplace</a>
</li>
<li class="user">
<a href="https://home.openweathermap.org/">mjrotter</a>
</li>
<li>
<a class="logout" rel="nofollow" data-method="delete" href="https://home.openweathermap.org/users/sign_out">Logout
</a></li>
</ul>
</nav>
<!-- Invisible header to take up the height -->
<div style="height: 48pt; width: 100%; visibility: hidden;"></div>

<div class="wrapper">
<div id="alert_body"></div>
<div id="flash"></div>

<div class="container">

<div class="row">
<div class="col-md-12">
<div class="clearfix">
<ul class="nav nav-tabs pull-left" id="myTab">
<li class="">
<a href="https://home.openweathermap.org/">New Products</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/myservices">Services</a>
</li>
<li class="active">
<a href="https://home.openweathermap.org/api_keys">API keys</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/subscriptions">Billing plans</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/payments">Payments</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/blocks">Block logs</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/marketplace/my_orders">My orders</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/home">My profile</a>
</li>
<li class="">
<a href="https://home.openweathermap.org/questions">Ask a question</a>
</li>
</ul>
</div>
</div>
</div>

<div class="alert alert-info">
You can generate as many API keys as needed for your subscription. We accumulate the total load from all of them.
</div>
<br>
<div class="row">
<div class="col-xs-7">
<table class="material_table api-keys">
<thead>
<tr>
<th>Key</th>
<th>Name</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>dd2b6cd880ea027d7a29580e87ad15bc</pre>
</td>
<td>keyweather</td>
<td class="text-center">
<a class="edit_key_btn edit-key-btn" data-action="/api_keys/60e89acfc51bce0007faf9ba" data-name="keyweather">
<i class="fa fa-edit"></i>
</a>
</td>
</tr>
</tbody>
</table>
</div>
<div class="col-xs-5">
<h4 style="border-bottom: 1px solid #f2f2f2; padding-bottom: 8pt;">Create key</h4>
<form class="new_api_key_form" id="new_api_key_form" action="https://home.openweathermap.org/api_keys" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="TqIgc0q/Dh0VuFrgLjB9qkA1DprdiJAlS6hlGk3XUsxN7C+Xl2BxwxR89iAoT7uv/zCtbKfeZegNYxTyXAZjig=="><input placeholder="API key name" class="owm_input" required="required" maxlength="20" style="margin-left: 0;" size="20" type="text" name="api_key_form[name]" id="api_key_form_name">
<input type="submit" name="commit" value="Generate" class="button-round dark" data-disable-with="Create Api key form">
</form></div>
</div>
<div class="modal fade" id="edit_key_modal">
<div class="pop-up-container">
<div class="pop-up-header">
<h3>Edit API key name</h3>
<a data-dismiss="modal">
<img src="./api_files/icon_close-e694b2773c0e76d9b340720de987954782bda13b140420733cb3d5b959e48136.svg" alt="Icon close">
</a>
</div>
<div class="pop-up-content">
<form class="new_edit_key_form" id="new_edit_key_form" action="https://home.openweathermap.org/api_keys" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="_method" value="patch"><input type="hidden" name="authenticity_token" value="TqIgc0q/Dh0VuFrgLjB9qkA1DprdiJAlS6hlGk3XUsxN7C+Xl2BxwxR89iAoT7uv/zCtbKfeZegNYxTyXAZjig=="><label for="edit_key_form_name">API key name</label>
<input class="owm_input" maxlength="20" size="20" type="text" name="edit_key_form[name]" id="edit_key_form_name">
</form></div>
<div class="pop-up-footer">
<button class="button-round transparent" data-dismiss="modal">Cancel</button>
<button class="button-round dark" onclick="$(&quot;#new_edit_key_form&quot;).submit()">Save</button>
</div>
</div>
</div>


</div>
</div>
<div class="footer-website" onclick="toggleFooterSection(event)">
<div class="inner-footer-container">
<div class="horizontal-section">
<div class="section">
<p class="section-heading">Product Collections</p>
<div class="section-content">
<ul>
<li>
<a href="http://openweathermap.org/api#current">Current and Forecast APIs</a>
</li>
<li>
<a href="http://openweathermap.org/api#history">Historical Weather Data</a>
</li>
<li>
<a href="http://openweathermap.org/api#maps">Weather Maps</a>
</li>
<li>
<a href="http://openweathermap.org/widgets-constructor">Widgets</a>
</li>
</ul>
</div>
</div>
<div class="section">
<p class="section-heading">Subscription</p>
<div class="section-content">
<ul>
<li>
<a href="http://openweathermap.org/appid">How to start</a>
</li>
<li>
<a href="http://openweathermap.org/price">Pricing</a>
</li>
<li>
<a href="https://home.openweathermap.org/users/sign_up">Subscribe for free</a>
</li>
<li>
<a href="https://openweathermap.org/faq">FAQ</a>
</li>
</ul>
</div>
</div>
<div class="section">
<span class="section-heading">
<a href="https://openweathermap.org/about-us">About us</a>
</span>
<div class="section-content">
<p>
OpenWeather is a team of IT experts and data scientists that has been practising deep
weather data science since 2014. For each point on the globe, OpenWeather provides
historical, current and forecasted weather data via light-speed APIs. Headquarters in London, UK.
</p>
</div>
</div>
</div>
<div class="horizontal-section">
<div class="section">
<p class="section-heading">Technologies</p>
<div class="section-content">
<ul>
<li>
<a href="http://openweathermap.org/technology">Weather models</a>
</li>
<li>
<a href="http://openweathermap.org/stations">Connect your weather station</a>
</li>
</ul>
</div>
</div>
<div class="section">
<p class="section-heading">Terms &amp; Conditions</p>
<div class="section-content">
<ul>
<li>
<a target="_blank" href="https://openweather.co.uk/storage/app/media/Terms/Openweather_terms_and_conditions_of_sale.pdf">Terms and conditions of sale</a>
</li>
<li>
<a target="_blank" href="https://openweather.co.uk/privacy-policy">Privacy Policy</a>
</li>
<li>
<a target="_blank" href="https://openweather.co.uk/storage/app/media/Terms/Openweather_website_terms_and_conditions_of_use.pdf">Website	terms	and	conditions</a>
</li>
</ul>
</div>
</div>
<div class="section not-foldable">
<p class="section-heading" style="visibility: hidden">Contact us</p>
<div class="section-content">
<ul>
<li>
<a target="_blank" href="https://openweather.co.uk/team">Our team</a>
</li>
<li>
<a target="_blank" href="https://openweather.co.uk/blog/category/weather">Blog</a>
</li>
<li>
<a href="https://home.openweathermap.org/questions">Ask a question</a>
</li>
<li>
<a href="mailto:info@openweathermap.org">info@openweathermap.org</a>
</li>
</ul>
</div>
</div>
</div>
<br>
<div>
<p style="margin: 0;">Download OpenWeather app</p>
<div style="display: flex; flex-direction: row;">
<a href="https://apps.apple.com/gb/app/openweather/id1535923697" style="margin-left: -10px;" target="_blank">
<img alt="Download on the AppStore" src="./api_files/Download_on_the_App_Store_Badge_US-UK.svg" style="height:60px; padding:10px;">
</a>
<a href="https://play.google.com/store/apps/details?id=uk.co.openweather" target="_blank">
<img alt="Get it on Google Play" src="./api_files/google-play-badge.png" style="height:60px;">
</a>
</div>
</div>
<div class="horizontal-section">
<p>© 2012 — 2021 OpenWeather ® All rights reserved.</p>
<div class="social">
<a target="_blank" href="https://www.facebook.com/groups/270748973021342"><img src="./api_files/icon_facebook-e4cf441116ca008e82e7b4ab7ecc3f1d6dbc8910970d37205904e9e26bff5331.png" alt="Icon facebook">
</a><a target="_blank" href="https://twitter.com/OpenWeatherMap"><img src="./api_files/icon_twitter-9d9bd503c1a756261893e4000fb15e1393436c639e27ceceee25253226e476b9.png" alt="Icon twitter">
</a><a target="_blank" href="https://www.linkedin.com/company/9816754"><img src="./api_files/icon_linkedin-e49a7283338c25d210a7608a6eb1e2373e8a7601790808be2161e8768c4fd2c4.png" alt="Icon linkedin">
</a><a target="_blank" href="https://medium.com/@openweathermap"><img src="./api_files/icon_medium-100f79c639f6b11bb4989b99b8fa7bb577fa31b031f1f9f9d4ce3dc06ddd8ee4.png" alt="Icon medium">
</a><a target="_blank" href="https://t.me/openweathermap"><img src="./api_files/icon_telegram-dd86dea60cf1250d4f65c0b1ccc2df8d4eb5de3380bb47a1a9a78049393ec1be.png" alt="Icon telegram">
</a><a target="_blank" href="https://github.com/search?q=openweathermap&amp;ref=cmdform"><img src="./api_files/icon_github-7d4574123bff8668e3b1d26aa1bb1b34857c360f960b3e2ea353875a3e0a347e.png" alt="Icon github">
</a></div>
</div>
</div>
</div>
<script>
  function toggleFooterSection (e) {
    if (e.target && (e.target.className === 'section-heading' || e.target.parentNode.className === 'section-heading')) {
      let section = e.target.className === 'section-heading' ? e.target.parentNode : e.target.parentNode.parentNode;
      if (section.classList.contains('visible')) {
        section.classList.remove('visible')
      } else {
        section.classList.add('visible')
      }
    }
  }
</script>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async="" src="./api_files/js"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-31601618-7');
</script>

<script src="./api_files/application-d44f525125e385e3bfedc4cae738d6fc336725bd8bcaadc5261de66e0c40c9c4.js.download"></script>



<div class="loader-layout" style="display: none;">
<div class="redirect">
<img src="./api_files/owm-b168522712c309b0319074cbd035ceb35a90d47dd9f01e622f2c76e7703181f3.gif" alt="Owm">
<p>
<b class="msg">Please wait...</b>
</p>
</div>
</div>


<div id="topcontrol" title="" style="position: fixed; bottom: 5px; right: 5px; opacity: 0; cursor: pointer;"><i class="fa fa-angle-up backtotop"></i></div></body></html>