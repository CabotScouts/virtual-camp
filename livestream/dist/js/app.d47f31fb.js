(function(e){function t(t){for(var r,c,u=t[0],o=t[1],s=t[2],f=0,d=[];f<u.length;f++)c=u[f],Object.prototype.hasOwnProperty.call(a,c)&&a[c]&&d.push(a[c][0]),a[c]=0;for(r in o)Object.prototype.hasOwnProperty.call(o,r)&&(e[r]=o[r]);l&&l(t);while(d.length)d.shift()();return i.push.apply(i,s||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,u=1;u<n.length;u++){var o=n[u];0!==a[o]&&(r=!1)}r&&(i.splice(t--,1),e=c(c.s=n[0]))}return e}var r={},a={app:0},i=[];function c(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.m=e,c.c=r,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)c.d(n,r,function(t){return e[t]}.bind(null,r));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="https://camp.cabotscouts.org.uk/_ls/";var u=window["webpackJsonp"]=window["webpackJsonp"]||[],o=u.push.bind(u);u.push=t,u=u.slice();for(var s=0;s<u.length;s++)t(u[s]);var l=o;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"16c6":function(e,t,n){},"23ec":function(e,t,n){},"30b8":function(e,t,n){"use strict";var r=n("37c6"),a=n.n(r);a.a},"37c6":function(e,t,n){},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("HeaderBar"),n("Wall"),n("FooterMarquee")],1)},i=[],c=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("header",[n("div",{attrs:{id:"logo"}},[e._v("Way Out West!")]),n("div",{attrs:{id:"clock"}},[n("time",[e._v(e._s(e.hours)),n("span",{staticClass:"sep"},[e._v(":")]),e._v(e._s(e.minutes))])])])},u=[],o=function(e){return e<10?"0"+e:e},s=function(){return new Date},l=function(){return o(s().getHours())},f=function(){return o(s().getMinutes())},d={name:"HeaderBar",data:function(){return{tick:null,hours:l(),minutes:f()}},created:function(){var e=this;this.tick=setInterval((function(){e.hours=l(),e.minutes=f()}),1e3)},destroyed:function(){clearInterval(this.tick)}},h=d,p=(n("7653"),n("2877")),v=Object(p["a"])(h,c,u,!1,null,null,null),m=v.exports,g=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("main",[n("transition",{attrs:{name:"fade"}},[e.current?n("div",{attrs:{id:"share",data:e.current}},[e.current.file?n("div",{staticClass:"media",class:e.current.type},["image"==e.current.type?n("img",{attrs:{src:e.current.file}}):e._e(),"video"==e.current.type?n("div",{staticClass:"video"},[n("video",{ref:"video",attrs:{src:e.current.file,autoplay:""}})]):e._e()]):e._e(),e.current.caption?n("div",{staticClass:"caption"},[n("p",[e._v(" "+e._s(e.current.caption)+" ")])]):e._e()]):e._e()])],1)},b=[],_=(n("d3b7"),n("96cf"),n("1da1")),y="https://camp.cabotscouts.org.uk/wall/shares/30";function x(e){return new Promise((function(t){return setTimeout(t,e)}))}var w={name:"Wall",data:function(){return{fetchTimer:null,changeTimer:null,media:[],current:{},currentIdx:-1,error:!1}},mounted:function(){var e=this;this.fetchMedia().then((function(){e.currentIdx=-1,e.changeTimer||e.changeMedia(),e.fetchTimer=setInterval((function(){return e.fetchMedia()}),3e5)}))},methods:{fetchMedia:function(){var e=this;return fetch(y).then((function(e){return e.json()})).then((function(t){e.media=t.media}))},changeMedia:function(){var e=Object(_["a"])(regeneratorRuntime.mark((function e(){var t=this;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return this.current=!1,e.next=3,x(1500);case 3:clearInterval(this.changeTimer),this.currentIdx=this.currentIdx+1==this.media.length?0:this.currentIdx+1,this.current=this.media[this.currentIdx],"video"==this.current.type?this.$nextTick((function(){t.$refs.video.addEventListener("loadedmetadata",(function(){t.media.length>1&&(t.changeTimer=setInterval((function(){return t.changeMedia()}),1e3*t.$refs["video"].duration+5e3)),t.$refs["video"].play()}))})):this.media.length>1&&(this.changeTimer=setInterval((function(){return t.changeMedia()}),3e4));case 7:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()}},M=w,O=(n("30b8"),Object(p["a"])(M,g,b,!1,null,null,null)),j=O.exports,I=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("footer",[n("marquee",{attrs:{scrollamount:"5"}},[e._v(e._s(e.message))])],1)},k=[],T="https://camp.cabotscouts.org.uk/wall/message",$={name:"FooterMarquee",data:function(){return{message:"",timer:null}},mounted:function(){var e=this;this.fetchMessage(),this.timer=setInterval((function(){return e.fetchMessage()}),12e4)},methods:{fetchMessage:function(){var e=this;fetch(T).then((function(e){return e.json()})).then((function(t){e.message=t.message}))}}},P=$,E=(n("e6ad"),Object(p["a"])(P,I,k,!1,null,null,null)),S=E.exports,W={name:"App",components:{HeaderBar:m,Wall:j,FooterMarquee:S}},q=W,C=(n("5c0b"),Object(p["a"])(q,a,i,!1,null,null,null)),H=C.exports;r["a"].config.productionTip=!1,new r["a"]({render:function(e){return e(H)}}).$mount("#app")},"5c0b":function(e,t,n){"use strict";var r=n("9c0c"),a=n.n(r);a.a},7653:function(e,t,n){"use strict";var r=n("16c6"),a=n.n(r);a.a},"9c0c":function(e,t,n){},e6ad:function(e,t,n){"use strict";var r=n("23ec"),a=n.n(r);a.a}});
//# sourceMappingURL=app.d47f31fb.js.map