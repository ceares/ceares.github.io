---
layout: post
title: LaTeX常见错误对照表
date: 2010-04-13
categories: blog
tags: [LaTeX,error]
description: LaTeX常见错误对照表
---

# 表一

<table border="1" style="text-align:left">
<tbody>
<tr>
<th>S.No</th>
<th>Class</th>
<th>Error Message</th>
<th>Cause of Error</th>
</tr>
<tr>
<td>1</td>
<td>e_des</td>
<td>! LaTeX Error: There's no line here to end</td>
<td>Usage of \\ at the end of a long label in 'description' environment</td>
</tr>
<tr>
<td>2</td>
<td>e_center</td>
<td>! LaTeX Error: There's no line here to end</td>
<td>Usage of \\ after the heading line in 'center' environment</td>
</tr>
<tr>
<td>3</td>
<td>e_foot</td>
<td>&nbsp;! Argument of \@sect has an extra }</td>
<td>Usage of a fragile command 'footnote' within \section</td>
</tr>
<tr>
<td>4</td>
<td>e_ragged</td>
<td>&nbsp;! Argument of \@caption has an extra }</td>
<td>Usage of \\ within \raggedright or \raggedleft environment</td>
</tr>
<tr>
<td>5</td>
<td>e_and</td>
<td>&nbsp;! Extra alignment tab has been changed to \cr</td>
<td>Too many &amp;s in a row of a table or array or eqnarray.</td>
</tr>
<tr>
<td>6</td>
<td>e_cline</td>
<td>&nbsp;! Extra alignment tab has been changed to \cr</td>
<td>Reference no non existing column in \cline</td>
</tr>
<tr>
<td>7</td>
<td>e_col</td>
<td>&nbsp;! Extra alignment tab has been changed to \cr.</td>
<td>Usage @ in tabular* environment</td>
</tr>
<tr>
<td>8</td>
<td>e_num</td>
<td>&nbsp;! Missing number treated as zero</td>
<td>Usage of non numeric parameter after \\</td>
</tr>
<tr>
<td>9</td>
<td>e_asterisk</td>
<td>Missing * at the end of the line</td>
<td>* is not printed when used without brace after \\</td>
</tr>
<tr>
<td>10</td>
<td>e_pbox_miss</td>
<td>&nbsp;! Missing number, treated as zero.</td>
<td>\parbox[t]{} ..Missing argument to parbox</td>
</tr>
<tr>
<td>11</td>
<td>e_mis_circle</td>
<td>&nbsp;! Missing number, treated as zero.</td>
<td>Missing numeric parameter to \circle</td>
</tr>
<tr>
<td>12</td>
<td>e_list</td>
<td>&nbsp;! Argument of \lst@next has an extra }</td>
<td>Usage of 1stlisting inside fragile command \parbox</td>
</tr>
<tr>
<td>13</td>
<td>e_capacity</td>
<td>&nbsp;! TeX capacity exceeded, sorry [input stack size=1500]</td>
<td>Usage of 1stlisting inside fragile command \parbox</td>
</tr>
<tr>
<td>14</td>
<td>e_runaway</td>
<td>Runaway argument?</td>
<td>Generally because of missing braces, e.g \cline{1-2 instead of \cline{1-2}</td>
</tr>
<tr>
<td>15</td>
<td>e_verbatim</td>
<td>Runaway argument?</td>
<td>Usage of verbatim within scope of another command e.g: \ifthenelse</td>
</tr>
<tr>
<td>16</td>
<td>e_undefined</td>
<td>! Undefined control sequence</td>
<td>Usage of an unknown command</td>
</tr>
<tr>
<td>17</td>
<td>e_footnote</td>
<td>! Undefined control sequence</td>
<td>Usage of \footnote within \footnote</td>
</tr>
<tr>
<td>18</td>
<td>e_integral</td>
<td>&nbsp;! Missing { inserted.</td>
<td>Integral bounds are malformed</td>
</tr>
<tr>
<td>19</td>
<td>e_zeta</td>
<td>&nbsp;! Missing { inserted.</td>
<td>Extra subscript before integral upper limit term</td>
</tr>
<tr>
<td>20</td>
<td>e_bezier</td>
<td>&nbsp;! Illegal unit of measure (pt inserted).</td>
<td>Missing numeric argument to \qbezier</td>
</tr>
<tr>
<td>21</td>
<td>e_too_bezier</td>
<td>&nbsp;! Illegal unit of measure (pt inserted).</td>
<td>Too many arguments to \qbezier</td>
</tr>
<tr>
<td>22</td>
<td>e_unit</td>
<td>&nbsp;! Illegal unit of measure (pt inserted)</td>
<td>\parbox[t]{2} ..Illegal unit of second parameter</td>
</tr>
<tr>
<td>23</td>
<td>e_symfoot</td>
<td>&nbsp;! LaTeX Error: Counter too large.</td>
<td>More than 9 footnotes when using symbolic footnotes</td>
</tr>
<tr>
<td>24</td>
<td>e_large_count</td>
<td>&nbsp;! LaTeX Error: Counter too large.</td>
<td>Trying to display a corresponding letter for a counter vallue &gt;26</td>
</tr>
<tr>
<td>25</td>
<td>e_begin</td>
<td>! LaTeX Error: Missing \begin{document}</td>
<td>Either text has been placed before \begin{document} or \begin{document} is missing</td>
</tr>
<tr>
<td>26</td>
<td>e_margin</td>
<td>&nbsp;! LaTeX Error: Missing \begin{document}.</td>
<td>Misuse of \marginsize</td>
</tr>
</tbody>
</table>

# 表二

<table border="1" style="text-align:left">
<tbody>
<tr>
<th>S.No</th>
<th>Class</th>
<th>Error Message</th>
<th>Cause of Error</th>
</tr>
<tr>
<td>1</td>
<td>e_fileEnd</td>
<td>! File ended while scanning use of \end.</td>
<td>Generally caused because of missing a brace</td>
</tr>
<tr>
<td>2</td>
<td>e_end</td>
<td>No message only an asterisk, i.e *</td>
<td>Missing \end{document}</td>
</tr>
<tr>
<td>3</td>
<td>e_illegal</td>
<td>LaTeX Error: Illegal character in array arg</td>
<td>Usage of a letter other than r,l and c in tabular environment</td>
</tr>
<tr>
<td>4</td>
<td>e_tab</td>
<td>! Misplaced alignment tab character &amp;</td>
<td>Missing \begin{tabular} while using tabular environment</td>
</tr>
<tr>
<td>5</td>
<td>e_backslash</td>
<td>! Missing \endcsname inserted</td>
<td>Usage of a backslash in front of the name of an environment, e.g \begin{\itemize}</td>
</tr>
<tr>
<td>6</td>
<td>e_delimiter</td>
<td>! LaTeX Error: Bad math environment delimiter</td>
<td>Missing \right immediately after the array environment</td>
</tr>
<tr>
<td>7</td>
<td>e_right</td>
<td>! Extra \right</td>
<td>\right has no matching \left OR \end{array} is missing</td>
</tr>
<tr>
<td>8</td>
<td>e_package</td>
<td>! LaTeX Error: Can only be used in preamble</td>
<td>Usage of \usepackage outside the preamble</td>
</tr>
<tr>
<td>9</td>
<td>e_math</td>
<td>! Missing $ inserted</td>
<td>Missing a starting or ending `$` in Math mode, e.g m_e instead of `$m_e$`</td>
</tr>
<tr>
<td>10</td>
<td>e_parameter</td>
<td>! Illegal parameter number in definition of...</td>
<td>Usage of parameter number greater than the number of parameters defined in \newcommand, e.g \newcommand{\test}[1]{#3}</td>
</tr>
<tr>
<td>11</td>
<td>e_cmd</td>
<td>! LaTeX Error: Command ... already defined</td>
<td>Trying to define already existing command, e.g \newcommand{\time}</td>
</tr>
<tr>
<td>12</td>
<td>e_caption</td>
<td>&nbsp;! LaTeX Error: \caption outside float</td>
<td>\caption{...} used outside table environment</td>
</tr>
<tr>
<td>13</td>
<td>e_braces</td>
<td>&nbsp;! Too many }'s</td>
<td>Missing \begin{table}statement</td>
</tr>
<tr>
<td>14</td>
<td>e_parbox</td>
<td>&nbsp;! Argument of \@caption has an extra }</td>
<td>Usage of \parbox in a \caption</td>
</tr>
<tr>
<td>15</td>
<td>e_item</td>
<td>&nbsp;! LaTeX Error: Something's wrong--perhaps a missing \item</td>
<td>Missing \item within enumerate environment</td>
</tr>
<tr>
<td>16</td>
<td>e_fraction</td>
<td>&nbsp;! Argument of \end has an extra }</td>
<td>Misuse of fraction cmd e.g \frac{1,2}</td>
</tr>
<tr>
<td>17</td>
<td>e_verb</td>
<td>&nbsp;! LaTeX Error: \verb ended by end of line</td>
<td>Newline after \verb, e.g. \verb*dir*</td>
</tr>
<tr>
<td>18</td>
<td>e_invalid</td>
<td>&nbsp;! LaTeX Error: Command \end{itemize} invalid in math mode</td>
<td>Missing $ while using math mode in \itemize</td>
</tr>
<tr>
<td>19</td>
<td>e_equation</td>
<td>&nbsp;! Display math should end with $$</td>
<td>Usage of $$ inside equation mode</td>
</tr>
<tr>
<td>20</td>
<td>e_column</td>
<td>&nbsp;! Misplaced \omit</td>
<td>Usage of \newcommand and \multicolumn within tabular environment</td>
</tr>
<tr>
<td>21</td>
<td>e_subscript</td>
<td>&nbsp;! Double subscript.</td>
<td>Usage of double subscript</td>
</tr>
<tr>
<td>22</td>
<td>e_cls</td>
<td>&nbsp;! LaTeX Error: File `artcle.cls' not found.</td>
<td>Missing .sty or .cls file</td>
</tr>
<tr>
<td>23</td>
<td>e_nofile</td>
<td>&nbsp;! LaTeX Error: File `file1.tex' not found.</td>
<td>Missing file1.tex, e.g. \input{file1.tex}</td>
</tr>
<tr>
<td>24</td>
<td>e_sty</td>
<td>&nbsp;! LaTeX Error: File `anysize1.sty' not found</td>
<td>Use of unavailable package</td>
</tr>
<tr>
<td>25</td>
<td>e_doc_class</td>
<td>&nbsp;! LaTeX Error: Can be used only in preamble.</td>
<td>Usage of \documentclass outside preamble</td>
</tr>
<tr>
<td>26</td>
<td>e_circle</td>
<td>&nbsp;! LaTeX Error: Command \circle invalid in math mode.</td>
<td>Usage of \circle in math mode</td>
</tr>
<tr>
<td>27</td>
<td>e_picture</td>
<td>&nbsp;! Use of \pictur@ doesn't match its definition.</td>
<td>Bad parameter to \picture</td>
</tr>
<tr>
<td>28</td>
<td>e_line</td>
<td>&nbsp;! Use of \put dosen't match its definition</td>
<td>Badly formatted \line directive</td>
</tr>
<tr>
<td>29</td>
<td>e_line_arg</td>
<td>&nbsp;! LaTeX Error: Bad \line or \vector argument.</td>
<td>Bad \line parameter</td>
</tr>
<tr>
<td>30</td>
<td>e_counter</td>
<td>&nbsp;! LaTeX Error: No counter '10' defined.</td>
<td>Counter undefined</td>
</tr>
<tr>
<td>31</td>
<td>e_outer</td>
<td>&nbsp;! LaTeX Error: Not in outer par mode.</td>
<td>Using figure inside parbox</td>
</tr>
<tr>
<td>32</td>
<td>e_minipage</td>
<td>&nbsp;! LaTeX Error: Not in outer par mode.</td>
<td>Using figure minipage</td>
</tr>
<tr>
<td>33</td>
<td>e_lost</td>
<td>&nbsp;! LaTeX Error: Float(s) lost.</td>
<td>Counter undefined</td>
</tr>
<tr>
<td>34</td>
<td>e_lonely</td>
<td>&nbsp;! LaTeX Error: Lonely \item--perhaps a missing list environment.</td>
<td>Usage of \item outside list environment</td>
</tr>
<tr>
<td>35</td>
<td>e_parg</td>
<td>&nbsp;! LaTeX Error: Missing p-arg in array arg.</td>
<td>Missing p argument in tabular environment</td>
</tr>
<tr>
<td>36</td>
<td>e_hash</td>
<td>&nbsp;! You can't use `macro parameter character #' in vertical mode.</td>
<td>Usage of # in normal mode</td>
</tr>
<tr>
<td>37</td>
<td>e_enlarge</td>
<td>&nbsp;! LaTeX Error: Suggested extra height (14454.0pt) dangerously large.</td>
<td>Too big a number given in \enlargethispage</td>
</tr>
<tr>
<td>38</td>
<td>e_deftab</td>
<td>&nbsp;! LaTeX Error: Undefined tab position.</td>
<td>Undefined tabbing</td>
</tr>
<tr>
<td>39</td>
<td>e_pushtab</td>
<td>&nbsp;! LaTeX Error: \pushtabs and \poptabs don't match.</td>
<td>Unequal numbers of push and pop tabs</td>
</tr>
<tr>
<td>40</td>
<td>e_overtab</td>
<td>&nbsp;! LaTeX Error: Tab overflow.</td>
<td>Too many \= in tabbing environment</td>
</tr>
<tr>
<td>41</td>
<td>e_nest</td>
<td>&nbsp;! LaTeX Error: Too deeply nested.</td>
<td>Too many list environments</td>
</tr>
<tr>
<td>42</td>
<td>e_eqnarray</td>
<td>&nbsp;! LaTeX Error: Too many columns in eqnarray environment.</td>
<td>More than three columns in eqnarray</td>
</tr>
<tr>
<td>43</td>
<td>e_classpkg</td>
<td>&nbsp;! LaTeX Error: \usepackage before \documentclass.</td>
<td>Usage of usepackage before loading documentclass</td>
</tr>
<tr>
<td>44</td>
<td>e_load</td>
<td>&nbsp;! LaTeX Error: Two \LoadClass commands.</td>
<td>More than one load class command</td>
</tr>
<tr>
<td>45</td>
<td>e_require</td>
<td>&nbsp;! LaTeX Error: \RequirePackage or \LoadClass in Options Section.</td>
<td>RequirePackage may not be used with \DeclareOption</td>
</tr>
<tr>
<td>46</td>
<td>e_twoclass</td>
<td>&nbsp;! LaTeX Error: Two \documentclass or \documentstyle commands.</td>
<td>More than one documentclass declaration</td>
</tr>
<tr>
<td>47</td>
<td>e_font</td>
<td>&nbsp;! LaTeX Error: This NFSS system isn't set up properly.</td>
<td>Invalid font used in \DeclareErrorFont</td>
</tr>
<tr>
<td>48</td>
<td>e_superscript</td>
<td>&nbsp;! Double superscript.</td>
<td>Usage of two superscripts for the same variable, e.g. 2^3^4</td>
</tr>
<tr>
<td>49</td>
<td>e_clash_opt</td>
<td>&nbsp;! LaTeX Error: Option clash for package csvtools.</td>
<td>Clashing options for the same package</td>
</tr>
<tr>
<td>50</td>
<td>e_unknown_opt</td>
<td>&nbsp;! LaTeX Error: Unknown option ... for package ...</td>
<td>Unkown option for a package</td>
</tr>
<tr>
<td>51</td>
<td>e_hyphenation</td>
<td>&nbsp;! Improper \hyphenation will be flushed.</td>
<td>Improper parameter to \hyphenation</td>
</tr>
<tr>
<td>52</td>
<td>e_stack_size</td>
<td>&nbsp;! TeX capacity exceeded, sorry [main memory size=1000000]</td>
<td>Overflow of buffer due to mistake in command definition</td>
</tr>
<tr>
<td>53</td>
<td>e_environment</td>
<td>&nbsp;! LaTeX Error: Environment ... undefined.</td>
<td>Undefined environment</td>
</tr>
<tr>
<td>54</td>
<td>e_midline</td>
<td>&nbsp;! LaTeX Error: \&lt; in mid line</td>
<td>Command \&lt; may appear only at the beginning of a line</td>
</tr>
<tr>
<td>55</td>
<td>e_infinite</td>
<td>Goes into infinite loop</td>
<td>Usage of \\strut\hrule</td>
</tr>
</tbody>
</table>
<hr>