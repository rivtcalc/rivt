#! python
'''rivtapi

    *rivtapi* is a module in *rivt*, a Python package designed to facilitate
    sharing and templating engineering calculation documents. It is imported at
    the beginning of a rivt calculation and includes four methods:

    R(rs) - repo and report information
    I(rs) - inserted text, images and static tables and math
    V(rs) - calculated values
    T(rs) - calculated tables and single line Python code

    where *rs* is a *rivtText* string. When running in an IDE (e.g. VSCode),
    each method can be run interactively using the standard cell decorator (#
    %%). If parameters are set in the file, or the entire calculation file is
    run from the command line, the formatted output is written to a utf8, PDF,
    or HTML file.

    The calculation input files are separated into two folders labeled *calc*
    and *files*. Files in the *calc* folder are shareable files under version
    control that contain the primary calculation and supporting text files. The
    *files* folder includes supporting binary files (images, pdf etc.) and files
    that include confidential project information or copyrights. The *files*
    folder is not intended to share.

    Output files are written to three places. The UTF8 calc output is
    written to a *readme.txt* file in the *calc* folder that is automatically
    displayed on source control platforms like GitHub. PDF output is written to
    *report*, and HTML output to the *site* folder.

    *rivtText* is a superset of the markup language reStructuredText (reST)
    defined at https://docutils.sourceforge.io/rst.html. It is designed for
    clarity, brevity and general platform reading and writing and processing.
    It runs on any platform that supports Python.

    The *rivtText* superset includes commands, tags and single line Python
    statements. Commands read or write files into and out of the calculation
    and start the line with ||. Tags format text and end a line with _[tag].
    Block tags start the block with [[tag]] and end with an [[end]] tag.

    *rivtDoc* is the complete open source software stack for writing, sharing
    and publishing engineering documents and calculations. The stack includes
    *Python*, Python science and engineering libraries, *VSCode* and
    extensions, *LaTeX (TexLive)*, *GitHub*, and *rivt*, and is available
    through installers.

    *rivt* command parameters are separated by |. In the summary below, user
    selections are separated by semi-colons for single value selections and
    commas for list settings. The first line of each method specifies
    formatting and labeling parameters for that calc or rivt-string. The method
    label can be a section or paragraph title, or used only for bookmarking and
    searching (see tags for syntax).

    ======= ===================================================================
     name              method, settings, snippet prefix
    ======= ===================================================================

    repo    rv.R("""label | folder;default | title | utf;pdf;html;int | width#n
    rvr
                 ||text ||table ||github ||project

                 """)

    insert  rv.I("""label | docs_folder;default
    rvi
                 ||text ||table ||image ||image2 ||attach

                 """)

    values  rv.V("""label | docs_folder;default | sub;nosub | save;nosave
    rvv
                 = ||values ||lists ||import

                 ||text ||table ||image ||image2 ||attach

                 """)

    tables  rv.T("""label | docs_folder;default | show;noshow
    rvt
                 Python simple statements
                 (any valid expression or statment on a single line)

                 ||text ||table ||image ||image2 ||attach

                 """)

    exclude rv.X("""  any text

                 any commands

                 """)

    =============================================================== ============
      rivt command syntax / snippet prefix and description             methods
    =============================================================== ============

    || github | repo_name | param1 | param                             R
        git        github repo parameters

    || project | file_name | /docsfolder; default                      R
        pro       .txt; rst; csv; syk; xls | project info folder

    || report | report title | cover page | default; file folder       R
        rep        .txt; rst; csv; syk; xls | project info folder

    || append | file_name | ./docfolder; default / resize;default      R
        app      .pdf; .txt | pdf folder / rescale to page size

    || list | file_name  | [:];[x:y]                                      V
        lis       .csv;.syk;.txt;.py | rows to import

    || values | file_name | [:];[x:y]                                      V
        val       .csv; .syk; .txt; .py | rows to import

    || functions | file_name | docs; nodocs                                V
        fun       .for; .py; .c; .c++; .jl | insert docstrings

    || image1 | file_name  | .50                                         I,V,T
        im1       .png; .jpg |  page width fraction

    || image2 | file_name  | .40 | file_name  | .40                      I,V,T
        im2       side by side images

    || text | file_name | shade; noshade                                 I,V,T
        tex      .txt; .py; .tex | shade background

    || table | file_name |  [:] | 60 r;l;c                               I,V,T
        tab      .csv;.rst file | rows | max col width, locate text

    =====================  =====================================================
      rivt tag syntax                       description: snippet prefix
    =====================  =====================================================

                tags for rivt-string first line settings

    """label | ....               label as section title, with autonumber
    """-label | ....              Single hyphen denotes paragraph title
    """--label | ....             Double hyphen denotes reference label only

                line tags for all methods:

    label _[e]{2,2}               equation label, decimals, autonumber: _e
    caption _[f]                  figure caption, autonumber: _f
    title _[t]                    table title, autonumber: _t
    heading _[p]                  paragraph heading: _p
    sympy eq _[s]                 format sympy equation: _s
    latex eq _[x]                 format LaTeX equation: _x
    text _[l]                     literal text: _l
    text _[r]                     right justify line of text: _r
    text _[c]                     center line of text: _c
    text _[-]                     horizontal line: _-
    text _[new]                   new PDF page: _n
    text _[#]                     footnote, autonumber: _#
    footnote _[foot]              footnote description: _o
    _[url]{address, label}        http://xyz, link label: _u
    _[lnk]{label}                 section, paragraph, title, caption: _k

                line tags that apply only to the Values method:

    a = b + c | unit, alt         = sign is tag for evaluation : _=
    a = n | unit, alt | descrip   units and description: _v

                block tags for all methods:

    _[[r]]                        right justify text block: _[[r
    _[[c]]                        center text block: _[[c
    _[[lit]]                      literal block: _[[l
    _[[tex]]                      LateX block: _[[x
    _[[texm]]                     LaTeX math block: _[[m
    _[[end]]                      terminates block: _[[e

                    block tag that applies only to the Repo method:

    _[[read]]                     write to README.txt in *calc* folder: _read

    Additional  VSCode shortcut keys and: snippet prefix

    ================== =========================================================
    shortcut                  description
    ================== =========================================================

    ctl+alt+x            reload window
    ctl+alt+u            unfold code
    ctl+alt+f            fold code - rivt file
    ctl+alt+a            fold code - all levels
    ctl+alt+t            toggle local fold at cursor
    ctl+alt+g            search accross GitHub rivt README: sgh
    ctl+alt+s            open URL under cursor in browser
    ctl+alt+-            insert general tag snippet

    ctl+8                toggle spell check
    ctl+.                select correct spelling under cursor

    ctl+0                focus explorer
    ctl+1                focus editor 1
    ctl+2                focus editor 2
    ctl+9                focus bookmark pane

    alt+q                wrap paragraph with hard line feeds


    [date]               insert date: dat
    [time]               insert time: tim
    [track]              insert time spent in VSCode: tra

    By convention the first line of a rivt file is *import rivtapi as rv*. The
    first method is the Repo method R(rs) which occurs once, followed by any of
    the other four methods in any number or order. R(rs) sets options for
    repository, report and calc output formats.

    Formatting conventions follow the Python formatter *pep8*. Method names
    start in column 1 and all subsequent lines are indented 4 spaces. This
    layout supports section folding and navigation, bookmarking and improved
    legibility.

    ============================================================================
    rivt calculation example
    ============================================================================

import rivt.rivtapi as rv

rv.R("""section label | Example Calculation | inter | 1

    The Repo method (short for repository or report) is the first method in a
    calc and specifies repository settings and output formats. It also typically
    includes a calculation summary.

    The setting line specifies the method, paragraph or section label, the calc
    title, the processing type and the starting page number for the output.

    The ||github command specifies settings for updating a public rivt repo.

    || github  | param1 | param2

    The ||project command imports data from the docs folder containing
    proprietary project data.  Its format depends on the file type.

    || project | file | default

    """)

rv.I("""Insert method summary | default

    The Insert method formats descriptive information as opposed to
    calculations and values that are stored during the calc processing.

    The ||text command inserts and processes text files of various types. Text
    files are always inserted as literal, without formatting.

    || text | file | shade

    Tags _[t] and _[f] format and autonumber tables and figures.

    table title  [t]_
    || table | file.csv; .rst; .syk | 60r;l;c

    || image | f1.png | 50
    A figure caption [f]_

    Insert two images side by side:

    || image2 | f2.png | 35 | f3.png | 45
    The first figure caption  [f]_
    The second figure caption  [f]_

    The tags [x]_ and [s]_ format LaTeX and sympy equations:

    \gamma = \frac{5}{x+y} + 3  [x]_
    x = 32 + (y/2)  [s]_

    The url tag formats a url link.
    _[http://wwww.url  label url]

    The link tag formats an internal document link to a table, equation,
    section or paragraph title:
    _["a calc title" link]

    Attach PDF documents at the end of the method:

    || attach | file | default | count

    """)

rv.V("""Value method summary | folder; default | nosub | save

    The Value method assigns values to variables and evaluates equations. The
    first setting is the section title. The sub;nosub setting specifies whether
    equations are output with substituted numerical values. The save;nosave
    setting specifies whether equations and value assignments are written to a
    values.txt file when the calc file is run. The values write is not triggered in
    interactive mode. The docfolder setting overrides the folder containing image

    The = tag in an expression triggers the evaluation of values and equations.
    A block of values terminated with a blank line are formatted into tables.

    a1 = 10.1    | unit, alt | description
    d1 = 12.1    | unit, alt | description

    Example equation tag - Area of circle  _[2,2]
    a1 = 3.14*(d1/2)^2 | unit, alt

    An equation tag; labels it with a description, auto numbers it, and
    specifies the printed decimal places in the equation and results. The
    equation tag is optional. Decimal places are retained until changed.

    The ||values command imports values from a csv or text file, where each row
    includes the variable name, value, primary unit, secondary unit, and
    description.

    || values | file | [:]

    The ||lists command inserts lists from a csv, text or Python file where the
    first column is the variable name and the subsequent values make up a
    vector of values assigned to the variable.

    || lists | file | [:]

    The ||functions method imports Python, Fortran, C or C++ functions. The
    function signature and doc strings are inserted into the calcs.

    || functions | file | docs;nodocs

    """
)
 rv.T("""Table method summary | default

    The Table method generates tables, plots and functions from native Python
    code. The method may include any Python simple statement (single line),
    rivt commands or tags. Any library imported at the top of the calc may be
    used, along with pandas, numpy, matplotlib and sympy library methods, which
    are imported by rivt. The four standard libraries import names are:

    pandas: pd.method()
    numpy: np.method()
    matplotlib: mp.method()
    sympy: sy.method()

    Common single line Python statements for defining functions or reading
    a file include:

    def f1(x,y): z = x + y; print(z); return

    with open('file.csv', 'r') as f: output = f.readlines()
    """
)
rv.X("""skip-string - can be anything.

    Skips evaluation of the string. Is used for review comments and debugging.
    """
) '''

import os
import sys
import subprocess
import time
import logging
import warnings
import shutil
import fnmatch
import numpy as np
from pathlib import Path
from collections import deque
import rivt.rv_r as rM
import rivt.rv_i as iM
import rivt.rv_v as vM
import rivt.rv_t as tM
import rivt.write as wrtM
import rivt.tags as tagM
import rivt.commands as cmdM

try:
    # print("argv1", sys.argv[1])
    docfileS = sys.argv[1]
except:
    # print("argv0", sys.argv[0])
    docfileS = sys.argv[0]
if ".py" not in docfileS:
    import __main__
    docfileS = __main__.__file__
    # print(dir(__main__))

# files and paths
docfileP = Path(docfileS)
cwdP = Path(os.getcwd())
docbaseS = docfileP.name  # calc file basename
docfolderP = Path(os.path.dirname(docfileP))
docP = docfolderP.parent  # calc folder path
rivtprojectP = docfolderP.parent.parent  # rivt project folder path
docbakP = docfolderP / ".".join((docbaseS, "bak"))
descripS = docbaseS.split("_")[1]
docconfigP = docP / "rv0000"

binfolderS = "b" + str(docbaseS[1:3])
binaryP = rivtprojectP / "binary"  # binary folder path
binfolderP = binaryP / binfolderS  # binary source folder
binconfigP = binaryP / "b00"  # file config folder

siteP = rivtprojectP / "site"  # site folder path
reportP = rivtprojectP / "reports"  # report folder path
rivtcalcP = Path("rivt.rivtapi.py").parent  # rivt package path
# initialize strings
utfS = """"""  # utf accumulating string
rstS = """"""  # reST accumulating string
valuexS = """"""  # export values accumulating string
# initialize dicts
rivtvalD = {}  # all persistent computed values
foldersD = {}  # folders
# folder names
for item in ["docfileP", "docconfigP", "binfolderP", "binconfigP", "reportP", "siteP"]:
    foldersD[item] = eval(item)
# tag settings
tagcountD = {
    "divnumS": docbaseS[1:3],  # division number
    "subnumS": docbaseS[3:5],  # subdivision number
    "docnumS": docbaseS[1:5],  # doc number
    "doctitleS": "rivt Document",  # doc title
    "methodtitleS": "rivt section",  # section title
    "secnumI": 0,  # section number
    "secwidthI": 80,  # utf section width
    "widthI": 77,  # utf body width
    "equI": 0,  # equation number
    "tableI": 0,  # table number
    "fignumI": 0,  # figure number
    "ftqueL": deque([1]),  # footnote number
    "countI": 0,  # footnote counter
    "decvI": 2,  # decimals for variables
    "decrI": 2,  # decimals for results
    "subsvalsB": False,  # substitute values
    "savevalsB": False  # save values to file
}
# run backups and logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    filename=docconfigP / "error_log.txt",
    filemode="w",
)
logconsole = logging.StreamHandler()
logconsole.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)-8s %(message)s")
logconsole.setFormatter(formatter)
logging.getLogger("").addHandler(logconsole)
warnings.filterwarnings("ignore")
dshortP = Path(*Path(docfolderP).parts[-2:])
bshortP = Path(*Path(binfolderP).parts[-2:])
lshortP = Path(*Path(binconfigP).parts[-2:])
# check that calc and file directories exist
if docfileP.exists():
    logging.info(f"""rivt file path : {docfileP}""")
else:
    logging.info(f"""rivt file path not found: {docfileP}""")

if binfolderP.exists:
    logging.info(f"""binary path: {binfolderP}""")
else:
    logging.info(f"""binary path not found: {binfolderP}""")
logging.info(f"""doc short path: {dshortP}""")
logging.info(f"""log short path: {lshortP}""")

# read calc file and write backup
with open(docfileP, "r") as f2:
    rivtS = f2.read()
    rivtL = f2.readlines()
with open(docbakP, "w") as f3:
    f3.write(rivtS)
logging.info("""rivt file read and backed up to text folder""")
print(" ")
# set some defaults
typesL = ["inter", "utf", "pdf", "html"]
rest_typeL = ["pdf", "html"]
typeS = "utf"
methodS = "R"
genrestB = False


def method_heading(riv1L: list, methodS: str):
    """format method headings - first line of string

    Args:
        hdrS (str): section heading line
    """

    global utfS, rstS, pubS, tagcountD, genrestB

    if riv1L[0][0:2] == "--":
        utfhS = "\n"
    elif riv1L[0][0:1] == "-":
        headS = riv1L[0][1:]
        utfhS = "\n" + headS + "\n"
    else:
        snumI = tagcountD["secnumI"]+1
        tagcountD["secnumI"] = snumI
        docnumS = "[" + tagcountD["docnumS"]+"]"
        methodS = tagcountD["methodtitleS"]
        compnumS = docnumS + " - " + str(snumI)
        widthI = tagcountD["widthI"]
        headS = " " + methodS + compnumS.rjust(widthI - len(methodS))
        bordrS = tagcountD["secwidthI"] * "_"
        utfhS = "\n" + bordrS + "\n\n" + headS + "\n" + bordrS + "\n"
        utfS += utfhS
        print(utfhS)

    if genrestB:
        # draw horizontal line
        rsthS = (
            ".. raw:: latex"
            + "\n\n"
            + "   ?x?vspace{.2in}"
            + "   ?x?textbf{"
            + methodS
            + "}"
            + "   ?x?hfill?x?textbf{SECTION "
            + compnumS
            + "}\n"
            + "   ?x?newline"
            + "   ?x?vspace{.05in}   {?x?color{black}?x?hrulefill}"
            + "\n\n"
        )
        rstS += rsthS


def R(rvrS: str):
    """processes a Repo string and sets output type

    R('''section lable | Calc title | utf;pdf;html;inter | page#
        Repo string commands.
        ||text, ||table, ||github, ||project, ||append, ||report
    ''')

    :param rvrS: triple quoted repo string
    :type rvrS: str
    :return: formatted utf or reST string
    :rtype: str
    """

    global utfS, rstS, valuexS, pubS, rivtvalD, foldersD, tagcountD, genrestB

    rvr1L = [None]*5
    rvr1L[0] = "rivt section"
    rvr1L[1] = "default"
    rvr1L[2] = "rivt Document"
    rvr1L[3] = pubS = "utf"
    rvr1L[4] = "80#1"
    methodS = "R"
    cmdL = cmdM.rvcmds("R")     # returns list of valid commands
    tagL = tagM.rvtags("R")     # returns list of valid tags
    rvL = rvrS.split("\n")     # list of rivt string lines
    rv1L = [i.strip() for i in rvL[0].split("|")]    # first line parameters

    # get_heading
    method_heading(rv1L, methodS)

    rvC = rM.R2utf()
    utfS += rvC.utf1(rvr1L)
    for i in rivtL[1:]:
        rS = rC.parseRutf(i)
        utfS += rS

    intercmdS = """print(utfS)"""

    utfcmdS = """
    utfoutP = Path(calcfileP / "README.txt")
    with open(utfoutP, "wb") as f1:
        f1.write(utfS.encode("UTF-8"))
    logging.info("utf calc written, program complete")
    print(utfS)
    print("", flush=True)
    os.exit(1)"""

    pdfcmdS = """
    rcalc = init(rvS)
    rcalcS, _setsectD = rcalc.r_rst()
    rstcalcS += rcalcS
    print("exit")
    os.exit(1)"""

    htmlcmdS = """
    rcalc = init(rvS)
    rcalcS, setsectD = rcalc.r_rst()
    rstcalcS += rcalcS
    os.exit(1)"""

    # generate reST file if needed
    if rvrL[1] in rest_typeL:
        rC = rM.parserest()
        genrstB = True
        wrtM.gen_rst(rivtL)

    # execute command string
    if rvr1L[1] in typesL:
        method_heading(typeS, rv1L)
        cmdS = rvr1L[1]+"cmdS"
        exec(cmdS)


def I(rviS: str):
    """processes an Insert string

    I('''section label | file folder; default

        Insert string commands.
        ||text, ||table, ||image1, ||image2
    ''')

    :param rviS: triple quoted insert string
    :type rviS: str
    :return: formatted utf or reST string
    :rtype: str
    """

    global utfS, rstS, valuexS, rivtvalD, foldersD, tagcountD, genrstB
    cmdL = cmdM.rvcmds("I")     # returns list of valid commands
    tagL = tagM.rvtags("I")     # returns list of valid tags
    rviL = rviS.split("\n")     # list of rivt string lines
    iC = iM._I2utf()

    if typeS == "inter":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += iC.i_utf(cmdL)
        print(utfS)


def V(rvvS: str):
    """processes a Value string

    V('''section label | file folder; default | sub; nosub | save; nosave

        Value string commands.
        ||text, ||table, ||image1, ||image2, || values, || list, || functions
    ''')

    :param rvvS: triple quoted values string
    :type rvvS: str
    :return: formatted utf or reST string
    :rtype: str
    """
    global utfS, rstS, valuexS, rivtvalD, foldersD, tagcountD, genrstB
    cmdL = cmdM.rvcmds("V")  # returns list of valid commands
    rvL = rvS.split("\n")  # line list of rivt string
    vC = vM._V2utf()

    if doctypeS == "term":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += vC.v_utf(cmdL)
        print(utfS)


def T(rvtS: str):
    """processes a Tables string

    T('''section label | file folder; default
        Table string commands
        ||text, ||table, ||image1, ||image2,
    ''')

    :param rvtS: triple quoted insert string
    :type rvtS: str
    :return: formatted utf or reST string
    :rtype: str

    """
    global utfS, rstS, rivtvalD, foldersD, tagL, cmdL, typeS, genrstB
    cmdL = cmdM.rvcmds("T")  # returns list of valid commands
    rvL = rvtS.split("\n")  # line list of rivt string
    tC = tM._T2utf()

    if doctypeS == "term":
        utfS += _tagM.tags(rvL[0])
        for i in rvL[1:]:
            utL = _tagM.tags(i, False)
            if utL[1]:
                utfS += utL[0]
                continue
            else:
                utfS += tC.t_utf(cmdL)
        print(utfS)


def X(rvxS: str):
    """processes an Exclude string

    X('''

        An exclude string can be any triple quoted string. It is used for review and debugging. To skip a rivt string processing, change R,I,V,T to X.
    ''')

    :param rvxS: triple quoted string
    :type rvxS: str
    """

    pass
