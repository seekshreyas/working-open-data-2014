# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Run all cells in this notebook, then run IPython:
# N
# 
# ```
# $ ipython notebook --profile solarized
# ```
# 
# Then remember to use ⌘-R to refresh your browser's cached css files

# <codecell>

profile_name = 'solarized-dark'

# <codecell>

!ipython profile create {profile_name}

# <codecell>

!ipython locate profile {profile_name}

# <codecell>

!mkdir ~/.ipython/profile_{profile_name}/static
!mkdir ~/.ipython/profile_{profile_name}/static/custom
!touch ~/.ipython/profile_{profile_name}/static/custom/custom.css

# <codecell>

%%file ~/.ipython/profile_{profile_name}/static/custom/custom.css

div#notebook {
    border-top: 1px solid #586e75;
}

/* cell areas */
div.input_area {
    background: #002b36;
    border: 1px solid #586e75;
}

div.text_cell_input {
    background: #002b36;
    border: 1px solid #586e75;

}

div.cell.selected {
    border-radius: 4px;
    border: thin #cb4b16 solid;
}

div.input_prompt {
    color: #93a1a1;
}

/* code cells */
.cm-s-ipython {
    background: #002b36;
    color: #839496;
    font-family:  CONSOLAS, ANDALE MONO, COURIER;
    font-size: 16px;
}

.cm-s-ipython span.cm-keyword {
    color: #859900;
    font-weight: bold;
}
.cm-s-ipython span.cm-number {
    color: #b58900;
}
.cm-s-ipython span.cm-operator {
    color: #268bd2; 
    font-weight: bold;
}
.cm-s-ipython span.cm-meta {
    color: #cb4b16;
}
.cm-s-ipython span.cm-comment {
    color: #586e75; 
    font-style: italic;
}
.cm-s-ipython span.cm-string {
    color: #2aa198;
}
.cm-s-ipython span.cm-error {
    color: #dc322f;
}
.cm-s-ipython span.cm-builtin {
    color: #cb4b16;
}
.cm-s-ipython span.cm-variable{
    color: #839496;
}

div.CodeMirror-cursor {
    border-left:solid 2px #93a1a1 !important;
}

/* output area */
div.output_text pre{
    color: #839496;
    font-size:16px;
}

div.output_html {
    color: #839496;
}

/* text/markdown cells */
div.text_cell div {
    color: #839496;
}

div.text_cell code {
    background-color: transparent;
}

div.text_cell pre {
    background-color: transparent;
}

/* nav bar */

.notification_widget {
    background: none;
    border: 1px solid #586e75;
}

# <codecell>


