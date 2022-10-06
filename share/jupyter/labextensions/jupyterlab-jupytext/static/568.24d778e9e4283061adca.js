"use strict";(self.webpackChunkjupyterlab_jupytext=self.webpackChunkjupyterlab_jupytext||[]).push([[568],{568:(t,e,o)=>{Object.defineProperty(e,"__esModule",{value:!0});const a=o(318),n=o(993),r=o(616),i=o(460),l=o(956),d=o(781),c=["ipynb","md","Rmd","qmd"];function u(t){if(!t.currentWidget)return[];let e=function(t){if(!t.currentWidget)return[];if(!t.currentWidget.context.model.metadata.has("jupytext"))return[];const e=t.currentWidget.context.model.metadata.get("jupytext");return(e&&e.formats?e.formats.split(","):[]).filter((function(t){return""!==t}))}(t);const o=t.currentWidget.context.model.metadata.get("language_info");if(o&&o.file_extension){const t=o.file_extension.substring(1);e=e.map((function(e){return e===t?"auto:light":e.replace(t+":","auto:")}))}let a=t.currentWidget.context.path.split(".").pop();if(!a)return e;a=-1==c.indexOf(a)?"auto":a;for(const t in e)if(e[t].split(":")[0]==a)return e;if(-1!=c.indexOf(a))e.push(a);else{let o="light";if(t.currentWidget.context.model.metadata.has("jupytext")){const e=t.currentWidget.context.model.metadata.get("jupytext");e&&e.text_representation&&e.text_representation.format_name&&(o=e.text_representation.format_name)}e.push("auto:"+o)}return e}const m={id:"jupyterlab-jupytext",autoStart:!0,optional:[l.ITranslator,a.ICommandPalette],requires:[r.NotebookPanel.IContentFactory,n.IEditorServices,i.IRenderMimeRegistry,a.ISessionContextDialogs,r.INotebookWidgetFactory,r.INotebookTracker],activate:(t,e,o,n,i,m,s,p,f)=>{var g,y,x;console.log("JupyterLab extension jupyterlab-jupytext is activated");const _=(null!=p?p:l.nullTranslator).load("jupytext"),b=function(t){return[{format:"ipynb",label:t.__("Pair Notebook with ipynb document")},{format:"auto:light",label:t.__("Pair Notebook with light Script")},{format:"auto:percent",label:t.__("Pair Notebook with percent Script")},{format:"auto:hydrogen",label:t.__("Pair Notebook with Hydrogen Script")},{format:"auto:nomarker",label:t.__("Pair Notebook with nomarker Script")},{format:"md",label:t.__("Pair Notebook with Markdown")},{format:"md:myst",label:t.__("Pair Notebook with MyST Markdown")},{format:"Rmd",label:t.__("Pair Notebook with R Markdown")},{format:"qmd",label:t.__("Pair Notebook with Quarto (qmd)")},{format:"custom",label:t.__("Custom pairing")},{format:"none",label:t.__("Unpair Notebook")}]}(_);b.forEach(((e,o)=>{const n=e.format,r="jupytext:"+n;t.commands.addCommand(r,{label:e.label,isToggled:()=>{if(!s.currentWidget)return!1;const t=u(s);if("custom"==n){for(const e in t){const o=t[e];if(-1==["ipynb","auto:light","auto:percent","auto:hydrogen","auto:nomarker","md","Rmd","qmd","md:myst"].indexOf(o))return!0}return!1}return-1!=t.indexOf(n)},isEnabled:()=>{if(!s.currentWidget)return!1;const t=s.currentWidget.context.path.split(".").pop();return n!==t&&("none"!==n||u(s).length>1)},execute:()=>{const t=s.currentWidget.context.model.metadata.get("jupytext");let e=u(s);if(console.log("Jupytext: executing command="+r),"custom"==n)return void a.showErrorMessage(_.__("Error"),_.__("Please edit the notebook metadata directly if you wish a custom configuration."));let o=s.currentWidget.context.path.split(".").pop();o=-1==c.indexOf(o)?"auto":o;const i=e.indexOf(n);if("none"===n)for(const t in e){const a=e[t];if(a.split(":")[0]===o){e=[a];break}}else if(-1!=i){e.splice(i,1);let t=!1;for(const a in e)if(e[a].split(":")[0]===o){t=!0;break}if(!t)return}else{const t=[];for(const o in e){const a=e[o];a.split(":")[0]!==n.split(":")[0]&&t.push(a)}e=t,e.push(n)}if(1===e.length)if("auto"!==o)e=[];else if(t&&t.text_representation){const o=e[0].split(":")[1];t.text_representation.format_name=o,e=[]}if(0===e.length){if(!s.currentWidget.context.model.metadata.has("jupytext"))return;return t.formats&&delete t.formats,void(0==Object.keys(t).length&&s.currentWidget.context.model.metadata.delete("jupytext"))}t?t.formats=e.join():s.currentWidget.context.model.metadata.set("jupytext",{formats:e.join()})}}),console.log("Jupytext: adding command="+r+" with rank="+(o+1)),null==f||f.addItem({command:r,rank:o+2,category:"Jupytext"})})),null==f||f.addItem({args:{text:_.__("Jupytext Reference"),url:"https://jupytext.readthedocs.io/en/latest/"},command:"help:open",category:"Jupytext",rank:0}),null==f||f.addItem({args:{text:_.__("Jupytext FAQ"),url:"https://jupytext.readthedocs.io/en/latest/faq.html"},command:"help:open",category:"Jupytext",rank:1}),t.commands.addCommand("jupytext_metadata",{label:_.__("Include Metadata"),isToggled:()=>!!s.currentWidget&&(!!s.currentWidget.context.model.metadata.has("jupytext")&&"-all"!==s.currentWidget.context.model.metadata.get("jupytext").notebook_metadata_filter),isEnabled:()=>{if(!s.currentWidget)return!1;if(!s.currentWidget.context.model.metadata.has("jupytext"))return!1;const t=s.currentWidget.context.model.metadata.get("jupytext");return void 0===t.notebook_metadata_filter||"-all"===t.notebook_metadata_filter},execute:()=>{if(console.log("Jupytext: toggling YAML header"),!s.currentWidget)return;if(!s.currentWidget.context.model.metadata.has("jupytext"))return;const t=s.currentWidget.context.model.metadata.get("jupytext");if(t.notebook_metadata_filter)return delete t.notebook_metadata_filter,void("-all"===t.cell_metadata_filter&&delete t.cell_metadata_filter);t.notebook_metadata_filter="-all",void 0===t.cell_metadata_filter&&(t.cell_metadata_filter="-all")}}),null==f||f.addItem({command:"jupytext_metadata",rank:b.length+3,category:"Jupytext"}),t.docRegistry.addFileType({name:"myst",displayName:_.__("MyST Markdown Notebook"),extensions:[".myst",".mystnb",".mnb"],icon:d.markdownIcon}),t.docRegistry.addFileType({name:"r-markdown",displayName:_.__("R Markdown Notebook"),extensions:[".rmd"],icon:d.markdownIcon}),t.docRegistry.addFileType({name:"quarto",displayName:_.__("Quarto Notebook"),extensions:[".qmd"],icon:d.markdownIcon});const k=new r.NotebookWidgetFactory({name:"Jupytext Notebook",fileTypes:["markdown","myst","r-markdown","quarto","julia","python","r"],modelName:null!==(g=m.modelName)&&void 0!==g?g:"notebook",preferKernel:null===(y=m.preferKernel)||void 0===y||y,canStartKernel:null===(x=m.canStartKernel)||void 0===x||x,rendermime:n,contentFactory:e,editorConfig:m.editorConfig,notebookConfig:m.notebookConfig,mimeTypeService:o.mimeTypeService,sessionDialogs:i,toolbarFactory:m.toolbarFactory,translator:p});t.docRegistry.addWidgetFactory(k);let h=0;const j=t.docRegistry.getFileType("notebook");k.widgetCreated.connect(((t,e)=>{var o,a;e.id=e.id||"notebook-jupytext-"+ ++h,e.title.icon=null==j?void 0:j.icon,e.title.iconClass=null!==(o=null==j?void 0:j.iconClass)&&void 0!==o?o:"",e.title.iconLabel=null!==(a=null==j?void 0:j.iconLabel)&&void 0!==a?a:"",e.context.pathChanged.connect((()=>{s.save(e)})),s.add(e)}))}};e.default=m}}]);