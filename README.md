<!DOCTYPE html>
<!-- Copyright Mycroft AI, Inc. 2017. All Rights Reserved. -->
<!-- Thanks to https://www.sanwebe.com/2014/08/css-html-forms-designs for the basis of this. -->
<html class="gr__rawgit_com" lang="en">

<style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Mobile Styles */

    @media only screen and (max-width: 400px) {
      .page {
        margin: 0 5% 0 5%;
      }
    }

    /* Tablet Styles */

    @media only screen and (min-width: 401px) and (max-width: 960px) {
      .page {
        margin: 0 10% 0 10%;
      }
    }

    /* Desktop Styles */

    @media only screen and (min-width: 961px) {
      .pageEdit {
        margin: 0 15% 0 15%;
      }
    }

    body {
      text-align: left;
      font-family: "Roboto";
      font-size: 16px;
      line-height: 1.5;
      color: #2c3e50;
      /* margin-right: 2em;
            margin-left: 2em; */
    }

    a {
      text-decoration: none;
      color: #22a7f0;
    }

    h1 {
      display: block;
      text-align: left;
      padding: 20px 0px;
      /* margin: 0 0; */
      color: #22a7f0;
      /* font-variant: small-caps; */
      font-size: 2.5em;
      font-weight: 900;
      line-height: 1.2;
    }

    h2 {
      color: #22a7f0;
      padding: 10px 0px;
      font-size: 1em;
      font-variant: small-caps;
      /*    text-transform: uppercase; */
      font-weight: 500;
    }

    p {
      padding: 0px 0px 30px 0px;
    }

    ol {
      list-style: none;
    }

    i {
      display: inline;
      color: #6c7a89;
      /* padding-right: 10px; */
    }

    .topnav {
      height: 64px;
      background-color: #22a7f0;
      margin-bottom: 0px;
      color: white;
      font-weight: 400;
      font-size: 18px;
      padding: 17px 20px;
    }

    .logo {
      margin-right: 10px;
      /* margin-top: 10px; */
    }

    .instructions {
      max-width: 100%;
      margin: 0px auto 30px auto;
      padding: 30px 50px 50px 50px;
      background-color: #c3d8e2 ;
      border-radius: 6px;
      line-height: 2;
    }

    .entry-form placeholder {
      background-color: #ff0000;
    }

    .entry-form {
      max-width: 100%;
      margin: 0px auto;
      background: #fff;
      border-radius: 6px;
      /* padding: 20px; */
      /* font-family: Georgia, "Times New Roman", Times, serif; */
    }

    .entry-form ul {
      list-style: none;
      padding: 0;
      margin: 0;
      /* background-color: ff0000; */
    }

    .entry-form li {
      display: block;
      padding: 8px 0px 0px 0px;
      border: 2px solid #c3d8e2 ;
      margin-bottom: 36px;
      border-radius: 6px;
      /* font-weight: bold; */
    }

    .entry-form li > label {
      display: block;
      /*    float: left; */
      /* margin-top: -19px; */
      background: #fff;
      /* height: 14px; */
      padding: 0px 10px;
      color: #22a7f0;
      font-size: 16px;
      overflow: hidden;
      font-family: "Roboto", "Helvetica", "Arial", sans-serif;
      font-weight: 500;
    }

    .entry-form input[type="text"],
    .entry-form input[type="date"],
    .entry-form input[type="datetime"],
    .entry-form input[type="email"],
    .entry-form input[type="number"],
    .entry-form input[type="search"],
    .entry-form input[type="time"],
    .entry-form input[type="url"],
    .entry-form input[type="password"],
    .entry-form textarea,
    .entry-form select {
      box-sizing: border-box;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      width: 100%;
      display: block;
      outline: none;
      border: none;
      /* height: 25px; */
      /* line-height: 25px; */
      font-size: 16px;
      padding: 12px 10px;
      font-family: "Roboto", "Helvetica", "Arial", sans-serif;
      color: #2c3e50;
    }

    .entry-form input[type="text"]:focus,
    .entry-form input[type="date"]:focus,
    .entry-form input[type="datetime"]:focus,
    .entry-form input[type="email"]:focus,
    .entry-form input[type="number"]:focus,
    .entry-form input[type="search"]:focus,
    .entry-form input[type="time"]:focus,
    .entry-form input[type="url"]:focus,
    .entry-form input[type="password"]:focus,
    .entry-form textarea:focus,
    .entry-form select:focus {
    }

    .entry-form li > span {
      background: #c3d8e2 ;
      display: block;
      padding: 8px 10px;
      /* margin: 0 -9px -9px -9px; */
      text-align: left;
      color: black;
      font-family: "Roboto", "Helvetica", "Arial", sans-serif;
      font-size: 13px;
    }

    .entry-form textarea {
      /* This is just Long Description field */
      resize: none;
      padding: 12px 10px;
      /* background-color: ff0000; */
      /* color: #ff0000; */
    }

    .device {
      padding-left: 20px;
      padding-bottom: 4px;
    }
    .category {
      padding-left: 20px;
      padding-bottom: 4px;
    }

    .first {
      padding-top: 8px;
    }

    #page_README input[type="button"] {
      background: #40dbb0;
      border: none;
      padding: 12px 20px;
      /* border-bottom: 3px solid #ff0000; */
      border-radius: 3px;
      color: #2c3e50;
      float:right;
      margin-bottom: 5px;
      margin-left: 5px;
    }

    #msgImportedREADME {
      color: rebeccapurple;
      float: right;
      padding-top: 6px;
    }

    #page_README input[type="button"]:hover {
      background: #fd9e66;
      cursor: pointer;
      color: #2c3e50;
    }

    #lblREADMENote {
      font-size: 75%;
      color: #22a7f0;
    }

    .entry-form .noborder {
      border: none;
      text-align: center;
      margin-bottom: 38px;
      margin-top: -8px;
    }

    .ex[id^="ex_"][name^="ex_"] {
      background: #fff;
      /* margin: 3px 0 3px 0; */
      padding: 12px 10px;
      margin-left: 20px;
      counter-reset: item;
      list-style-type: decimal;
    }
    .ex::before {
        content: "»";
        background-color: red;
        background: red;
        color: red;
    }

    .author[id^="author_"][name^="author_"] {
      background: #fff;
      /* margin: 3px 0 3px 0; */
      padding: 14px 10px;
      /* color: #ff0000; */
      /* font-weight: 900; */
    }

    input::placeholder {
      color: #AAAFB2;
      /* background-color: red; */
    }

    textarea::placeholder {
      color: #AAAFB2;
    }

    #custom_sections {
        height: 200px;
    }

    code {
      font-family: monospace;
      /* display: none; */
    }

    #rawREADME {
      width: 100%;
      height: 60vh;
    }

    #github_preview_frame {
        width: 100%;
        height: 60vh;
    }

    .primary_category span {
        color: black;
        font-weight: 900;
    }

    tt {
        font-family: monospace;
        font-size: 0.9em;
        font-weight: 700;
    }

    .card {
        /* Add shadows to create the "card" effect */
        box-shadow: 2px 4px 8px 2px rgba(0,0,0,0.2);
        border-radius: 5px; /* 5px rounded corners */
        padding: 2px 16px;
    }
    .card:hover {
        box-shadow: 2px 8px 16px 2px rgba(0,0,0,0.2);
    }

    .card_content {
        height: 100%;
    overflow: hidden;
    }

    .icon {
        width: 50px;
        height: 50px;
        font-size: 50px;

    }
    /**********************/
    /* Small card preview */
    /**********************/
    #card_small_category {
        font-size: 30px;
        color: #FD9E66;
    }

    #card_small_preview {
        width: 320px;
        height: 260px;
        padding: 10px;
        position: relative;
    }
    #title_small {
        font-size: 30px;
        margin-bottom: 5px;
        font-family: 'Roboto Mono',monospace;
        font-weight: 700;
        font-size: 24px;
        text-align: center;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }
    #utt_small {
        background-color: #E4F1FE;
        width: 260px;
        padding: 5px;
        margin-bottom: 15px;
        border-radius: 3px;
    }
    .utt_large {
        background-color: #E4F1FE;
        padding: 5px;
        border-radius: 3px;
    }

    #card_small_preview input[type="button"] {
      border: none;
      padding: 12px 20px;
      /* border-bottom: 3px solid #ff0000; */
      border-radius: 3px;
      background: #cccccc;

      width: 260px;
      position: absolute;
      bottom: 20px;
    }

    /**********************/
    /* Large card preview */
    /**********************/

    #cardb_large_preview {
        width: 700px;
        min-height: 500px;
        padding: 20px;
        position: relative;
    }

    #cardb_large_title {
        background: #dddddd;
        padding: 10px;
        margin: 0;
    margin-bottom: 10px;
    }

    #desc_large {
        margin-left: 70px;
    }

    #cardb_large_preview input[type="button"] {
      border: none;
      padding: 12px 20px;
      /* border-bottom: 3px solid #ff0000; */
      border-radius: 3px;
      background: #cccccc;

      width: 260px;
      position: absolute;
      bottom: 20px;
      right: 20px;
    }

    #div_fulldesc_large {
    margin-top: 15px;
        margin-bottom: 50px;
    }

    #by_large {
      position: absolute;
      bottom: 20px;
      left: 20px;
    }

    #title_large {
        font-size: 30px;
        margin-bottom: 5px;
    }

    /******************/
    /* Style the tabs */
    /******************/
    .tab {
        overflow: hidden;
        border: 1px solid #ccc;
        background-color: #f1f1f1;
    }

    /* Style the buttons that are used to open the tab content */
    .tab button {
        background-color: inherit;
        float: left;
        border: none;
        outline: none;
        cursor: pointer;
        padding: 1px 8px;
        height: 3em;
        transition: 0.3s;
    }

    /* Change background color of buttons on hover */
    .tab button:hover {
        background-color: #ddd;
    }

    /* Create an active/current tablink class */
    .tab button.active {
        background-color: #ccc;
        font-weight: 900;
    }

    /* Style the tab content */
    .tabcontent {
        display: none;
        padding: 6px 12px;
        xxborder: 1px solid #ccc;
        xxborder-top: none;
    }
</style>

<head>
  <meta http-equiv='Content-Type' content='text/html' ; charset='UTF-8'>
  <title>Mycroft Skill Readme Generator</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,500,700,900">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">

  <script type="application/javascript" src="https://cdn.jsdelivr.net/npm/commonmark@0.28.1/dist/commonmark.js"></script>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pickr-widget/dist/pickr.min.css"/>
  <script src="https://cdn.jsdelivr.net/npm/pickr-widget/dist/pickr.min.js"></script>

  <script type="text/javascript">

var colorPicker = null;
    //auto expand textarea
function adjust_textarea(h) {
  new_height = h.scrollHeight;
  if (new_height < 130) {
    new_height = 130;
  }
  h.style.height = "20px";
  h.style.height = new_height + "px";
}

///////////////////////////////////////////////////////////////////////////////
// Helpers

function strip(s){
  return ( s || '' ).trim();
}

String.prototype.replaceAll = function(search, replace)
{
    //if replace is not sent, return original string otherwise it will
    //replace search string with 'undefined'.
    if (replace === undefined) {
        return this.toString();
    }

    return this.replace(new RegExp('[' + search + ']', 'g'), replace);
};

///////////////////////////////////////////////////////////////////////////////
// README.md -> form

function showREADMEImport() {
  document.getElementById("msgImportedREADME").style.display = "block";
}

function hideREADMEImport() {
  document.getElementById("msgImportedREADME").style.display = "none";
}

function parseREADME() {
  // Take a README and populate the appropriate editor elements
  var text = document.getElementById("rawREADME").value;
  var sections = extract_sections(text);

  // Extract title, short desc and icon
  title_info = find_title_info(sections);
  document.getElementById("name").value = title_info[0];
  document.getElementById("short_desc").value = title_info[1];

  if (title_info[2])
    document.getElementById("icon").value = title_info[2];
  else {
    if (title_info[3])
      document.getElementById("icon").value = title_info[3];
    if (title_info[4])
      colorPicker.setColor(title_info[4]);
  }

  // Extract long desc
  document.getElementById("long_desc").value = find_section("About", sections) || find_section("Description", sections);
  adjust_textarea(document.getElementById("long_desc"));

  // Extract platform
  platform = find_section("Supported Devices", sections) || '';
  document.getElementById("req_mark1").checked = (platform.indexOf("platform_mark1") != -1);
  document.getElementById("req_mark2").checked = (platform.indexOf("platform_mark2") != -1);
  document.getElementById("req_picroft").checked = (platform.indexOf("platform_picroft") != -1);
  document.getElementById("req_plasmoid").checked = (platform.indexOf("platform_plasmoid") != -1);
  checkDevices();
  // Warn if platform is not found
  leftovers = strip(platform.replace("platform_mark1", "").replace("platform_mark2", "").replace("platform_picroft", "").replace("platform_plasmoid", ""));
  if (leftovers.length > 0)
    alert("WARNING: Nonstandard platform ("+leftovers+") will be lost.");

  // Parse Categories
  var categories = find_section("Category", sections) || "";
  leftovers = categories;
  var categoryEl = document.getElementsByClassName("category_section");
  for (var i = 0; i < categoryEl.length; i++) {
    id = categoryEl[i].id;
    name = id.substring(4);  // skip "cat_"
    if (categories.indexOf(name) != -1)
    {
      categoryEl[i].checked = true;
      if (categories.indexOf("**"+name+"**") != -1) {
        document.getElementById("for_"+id).className = "primary_category";
        leftovers = leftovers.replace("**"+name+"**", "");
      }
      else {
        document.getElementById("for_"+id).className = "";
        leftovers = leftovers.replace(name, "");
      }
    } else {
      categoryEl[i].checked = false;
      document.getElementById("for_"+id).className = "";
    }
  }
  // Warn if category is not found
  leftovers = strip(leftovers);
  if (leftovers.length > 0)
    alert("WARNING: Nonstandard category ("+leftovers+") will be lost.");

  // Parse Tags
  var tags = (find_section("Tags", sections) || "").split("\n");
  var tagParent = document.getElementById("all_tags");
  tagParent.innerHTML = '<label for="tag_1">Tags</label>'+
                        '<input class="tag" type="text" id="tag_1" maxlength="100" placeholder="#Tag 1" onkeyup="addNext(this, \'tag_\')" onchange="validateTag(this)"/>'+
                                  '<span>Tags are single word identifiers, such as #kids, #crypto and are used for searching.</span>';
  var elTag = document.getElementById("tag_1");
  for (var i = 0; i < tags.length; i++) {
    elTag.value = strip(tags[i]);
    elTag = addNext(elTag, 'tag_');
  }


  // Parse Examples
  var examples = (find_section("Examples", sections) || "").split("\n");
  var exParent = document.getElementById("all_ex");
  exParent.innerHTML = '<label for="ex_1">User Phrases: Hey Mycroft...</label>'+
                             '<input class="ex" type="text" id="ex_1" maxlength="100" placeholder="Phrase 1" onkeyup="addNext(this, \'ex_\')"/>'+
                                 '<span>Provide examples of phrases handled by the Skill after the Wake Word is spoken. The first may be highlighted and should be a prime example.<br/>Ex: "play the news", "set a 10-minute timer"</span>';
  var elEx = document.getElementById("ex_1");
  for (var i = 0; i < examples.length; i++) {
    elEx.value = strip(examples[i].replaceAll('"', "").replaceAll('*', ""));
    "".repl
    elEx = addNext(elEx, 'ex_');
  }

  // Parse Credits
  var credits = (find_section("Credits", sections) || "").split("\n");
  var elCredits = document.getElementById("all_authors");
  elCredits.innerHTML = '<label for="author_1">Author(s)</label>'+
                                  '<input class="author" type="text" id="author_1" maxlength="100" placeholder="Author name (@github_handle) 1" onkeyup="addNext(this, \'author_\')"/>'+
                                  '<span>Credits for people or organizations involved (name, email, and/or GitHub @handle).</span>';
  var elCredit = document.getElementById("author_1");
  for (var i = 0; i < credits.length; i++) {
    elCredit.value = strip(credits[i]);
    elCredit = addNext(elCredit, 'author_1');
  }

  // Deal with any custom markdown sections
  var elCustom = document.getElementById("custom_sections");
  elCustom.value = "";
  for (var i=1; i < sections.length; i++)
  {
    title = sections[i][0];
    if (title.indexOf("About") >= 0 || title.indexOf("Examples") >= 0 ||
        title.indexOf("Credits") >= 0 || title.indexOf("Tags") >= 0 ||
        title.indexOf("Supported Devices") >= 0 ||
        title.indexOf("Category") >= 0 || title.indexOf("Tags") >= 0)
        continue;

    content = sections[1];
    if (elCustom.value != "")
        elCustom.value += "\n";

    elCustom.value += "## "+title + "\n" + sections[i][1];
  }
}

function find_section(name, sections)
{
  name = name.toLowerCase();
  for (var i=0; i < sections.length; i++)
  {
    section = sections[i];
    if (section[0].toLowerCase() == name)
      return sections[i][1];
  }

  return null;
}

function find_title_info(sections)
{
  if (sections.length == 0)
        return "";

  var iTitle = 0;   // Old scheme: use first section
  for (var i=0; i < sections.length; i++)
  {
    section = sections[i];
    if (section[0].indexOf("<img") != -1)
    {
      iTitle = i;
      break;
    }
  }

  // extract icon info
  var icon_parts = sections[iTitle][0].split("'");
  var prev = "";
  var url = null;
  var name = null;
  var color = null;
  for (var i=0; i < icon_parts.length; i++)
  {
    var part = strip(icon_parts[i]);
    if (prev.endsWith("src="))
      url = part;
    else if (prev.endsWith("card_color="))
      color = part;

    prev = part;
  }

  if (url && (url.startsWith("https://rawgithub.com/FortAwesome/Font-Awesome") ||
              url.startsWith("https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/")))
  {
    name = url.split('/').pop().split(".")[0]
    url = null;
  }

  title = strip(sections[iTitle][0].split("/>").pop());
  short_desc = strip(sections[iTitle][1]);

  return [title, short_desc, url, name, color];
}

function extract_sections(text)
{
  var lines = text.split("\n");
  var sections = []

  var section_title = "";
  var content = "";
  for (var i=0; i < lines.length; i++)
  {
    var line = strip(lines[i]);
    if (line.startsWith("# ") || line.startsWith("## "))
    {
        if (section_title || content)
            sections.push([section_title, content]);
        section_title = strip(line.substring(2));
        content = [];
    }
    else
    {
        if (content.length > 0)
          content += "\n"+line;
        else
          content = line;
    }
  }
  if (content != "")
    sections.push([section_title, content]);

  return sections;
}

///////////////////////////////////////////////////////////////////////////////
// form -> README.md

function generateREADME() {
  // Convert the filled-out form to a markdown description (README.md) for
  // the mycroft-skill on Github
  var elem = document.getElementById("rawREADME");
  var elIcon = document.getElementById("icon");
  var elName = document.getElementById("name");
  var elShortDesc = document.getElementById("short_desc");
  var elLongDesc = document.getElementById("long_desc");
  var elCustomSections = document.getElementById("custom_sections");

  if (elIcon.value.startsWith("http"))
    icon_url = elIcon.value;
  else
    icon_url = "https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/"+elIcon.value+".svg";

  markdown = "# <img src='"+icon_url+"' card_color='"+colorPicker.getColor().toHEX().toString()+"' width='50' height='50' style='vertical-align:bottom'/>";
  markdown += " " + elName.value + "\n";

  markdown += elShortDesc.value + "\n\n";
  markdown += "## About\n";
  markdown += elLongDesc.value + "\n\n";

  markdown += "## Examples\n";
  for (var i = 1; ; i++) {
    var ex = document.getElementById("ex_" + i);
    if (!ex) break;
    if (ex.value != "") markdown += '* "' + ex.value + '"\n';
  }

  markdown += "\n## Credits\n";
  for (var i = 1; ; i++) {
    var ex = document.getElementById("author_" + i);
    if (!ex) break;
    if (ex.value != "") markdown += ex.value + "\n";
  }

  var req_mark1 = document.getElementById("req_mark1").checked;
  var req_mark2 = document.getElementById("req_mark2").checked;
  var req_picroft = document.getElementById("req_picroft").checked;
  var req_plasmoid = document.getElementById("req_plasmoid").checked;
  if (req_mark1 || req_mark2 || req_picroft || req_plasmoid) {
    markdown += "\n## Supported Devices \n";
    if (req_mark1) markdown += "platform_mark1 ";
    if (req_mark2) markdown += "platform_mark2 ";
    if (req_picroft) markdown += "platform_picroft ";
    if (req_plasmoid) markdown += "platform_plasmoid ";
    markdown += "\n";
  }

  var categoryEl = document.getElementsByClassName("category_section");
  markdown += "\n## Category\n";
  for (var i = 0; i < categoryEl.length; i++) {
    if (categoryEl[i].checked)
    {
        id = categoryEl[i].id;
        category = id.substring(4);  // skip "cat_"

        if (document.getElementById("for_"+id).className.includes("primary_category"))
            markdown += "**" + category + "**\n";
        else
            markdown += category + "\n";
    }
  }

  if (!validateCategories())
      markdown +="WARNING: You have no Categories selected. Please ensure your Skill is assigned to at least one Category." + "\n";


  var tagEl = document.getElementsByClassName("tag");
  markdown += "\n## Tags\n";
  for (var i = 1; ; i++) {
      var tag = document.getElementById("tag_" + i);
      if (!tag)
          break;
      if (tag.value != "")
          markdown += tag.value + "\n";
  }

  if (elCustomSections.value)
      markdown += "\n\n" + elCustomSections.value;

  hideREADMEImport();

  elem.value = markdown;
}

function addNext(input, id_prefix) {
  if (input.value == "")
    return null;

  inputNext = input.cloneNode(true);
  input.onkeyup = "";

  // ## <input class="ex" type="text" id="ex_1" maxlength="100" placeholder="example 1"...
  num = input.id.substring(id_prefix.length) * 1 + 1;

  inputNext.id = id_prefix + num;
  inputNext.value = "";

  if (input.placeholder) {
    placeholder_prefix = input.placeholder.substring(0, input.placeholder.length - (''+(num-1)).length)
    inputNext.placeholder = placeholder_prefix + num;
  }

  // Add after the last
  input.parentElement.insertBefore(inputNext, input.nextSibling);
  return inputNext;
}

function validateTag(elem)
{
    if (elem.value[0] != '#')
        elem.value = '#'+elem.value;
    elem.value = elem.value.replace(/ /g, "");
}

function validateCategories(){
  var categories = document.getElementsByClassName('category_section');
  var cCategories = 0;
  for (var i = 0; i < categories.length; i++) {
    if (categories[i].checked)
       return true;
  }

  return false;
}

function categoryClick(cb) {
  var elements = document.getElementsByClassName("category_section");

  var checks = 0;
  var iChecked = null;

  for (var i = 0; i < elements.length; i++) {

    if (elements[i].checked) {
      checks++;
      iChecked = i;
    }

    // TODO: Remove this logic?
    if (elements[i].id === "suggest") {
        if (elements[i].value !== "") {
            checks++;
        }
    }
  }

  if (checks <= 1) {
        for (var i = 0; i < elements.length; i++) {
        var label = document.getElementById("for_"+elements[i].id);
        if (label)
            if (i == iChecked)
                label.className = "primary_category";
            else
                label.className = "";
        }
  }
}

function toTab(evt) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById("page_"+evt.currentTarget.id).style.display = "block";
    evt.currentTarget.className += " active";
}

function generatePreviewCard()
{
  var elCategory = document.getElementById("card_small_category");
  var categoryEl = document.getElementsByClassName("category_section");
  var cat = "";

  for (var i = 0; i < categoryEl.length; i++) {
    if (categoryEl[i].checked)
    {
        id = categoryEl[i].id;
        category = id.substring(4);  // skip "cat_"

        if (document.getElementById("for_"+id).className.includes("primary_category")) {
            cat = category;
            break;
        }
    }
  }
  document.getElementById("card_small_category").innerText = cat;


  var elName = document.getElementById("name");
  document.getElementById("title_small").innerText = elName.value;

  var elShortDesc = document.getElementById("short_desc");
  document.getElementById("desc_small").innerText = elShortDesc.value;

  var elUtt0 = document.getElementById("ex_1");
  document.getElementById("utt_0_small").innerText = elUtt0.value;

  // TODO: Validate icon and color
  var elIcon = document.getElementById("icon");
  if (elIcon.value.startsWith("http"))
  {
    document.getElementById("img_icon_small").src = elIcon.value;
    document.getElementById("img_icon_small").style.display = "inline";
    document.getElementById("icon_small").style.display = "none";
  }
  else
  {
      document.getElementById("icon_small").className = "fa-3x fas fa-"+elIcon.value;
      document.getElementById("icon_small").style.color= colorPicker.getColor().toHEX().toString();
      document.getElementById("img_icon_small").style.display = "none";
      document.getElementById("icon_small").style.display = "inline";
  }
}

function generatePreviewDetail()
{
  var elName = document.getElementById("name");
  document.getElementById("title_large").innerText = elName.value;

  var elShortDesc = document.getElementById("short_desc");
  document.getElementById("desc_large").innerText = elShortDesc.value;

  var elLongDesc = document.getElementById("long_desc");
  document.getElementById("fulldesc_large").innerText = elLongDesc.value;


  // TODO: All authors
  var elAuthor = document.getElementById("author_1");
  document.getElementById("author_large").innerText = elAuthor.value;

  var phrases = "";
  for (var i = 1; ; i++) {
    var ex = document.getElementById("ex_" + i);
    if (!ex) break;
    if (ex.value)
        phrases += "<span class='utt_large'>"+ex.value+"</span> ";
  }
  document.getElementById("utt_1_large").innerHTML = phrases;


  // TODO: Validate icon and color
  var elIcon = document.getElementById("icon");
  document.getElementById("icon_large").className = "fa-3x fas fa-"+elIcon.value;
  document.getElementById("icon_large").style.color= colorPicker.getColor().toHEX().toString();

  if (elIcon.value.startsWith("http"))
  {
    document.getElementById("img_icon_large").src = elIcon.value;
    document.getElementById("img_icon_large").style.display = "inline";
    document.getElementById("icon_large").style.display = "none";
  }
  else
  {
      document.getElementById("icon_large").className = "fa-3x fas fa-"+elIcon.value;
      document.getElementById("icon_large").style.color= colorPicker.getColor().toHEX().toString();
      document.getElementById("img_icon_large").style.display = "none";
      document.getElementById("icon_large").style.display = "inline";
  }
}

function generatePreview()
{
    var elem = document.getElementById("rawREADME");

    var reader = new commonmark.Parser();
    var writer = new commonmark.HtmlRenderer();
    var parsed = reader.parse(elem.value); // parsed is a 'Node' tree

    // transform parsed if you like...
    var result = writer.render(parsed); // result is a String

    // Get the CSS used by Github to render
    fetch("https://raw.githubusercontent.com/sindresorhus/github-markdown-css/gh-pages/github-markdown.css").then(function(response) {
      response.text().then(function(githubcss) {
            var preview2 = document.getElementById("github_preview_frame");
            preview2.src = "data:text/html;charset=utf-8," +
                            escape("<!doctype html><html><style>"+githubcss+"</style><body>"+
                            "<article class='markdown-body'>"+result+"</article"+
                            "</body></html>");
      });
    });
}

function checkAllDevices()
{
    if (document.getElementById("support_all").checked)
    {
        document.getElementById("req_mark1").checked = false;
        document.getElementById("req_mark2").checked = false;
        document.getElementById("req_picroft").checked = false;
        document.getElementById("req_plasmoid").checked = false;
    }
}

function checkDevices()
{
    if (document.getElementById("req_mark1").checked ||
        document.getElementById("req_mark2").checked ||
        document.getElementById("req_picroft").checked ||
        document.getElementById("req_plasmoid").checked)
    {
        document.getElementById("support_all").checked = false;
        document.getElementById("support_specific").checked = true;
    }
    else
    {
        document.getElementById("support_all").checked = true;
        document.getElementById("support_specific").checked = false;
    }
}

function update_icon()
{
    var elIcon = document.getElementById("icon");

    var elPreview = document.getElementById("icon_preview");
    var elImgPreview = document.getElementById("img_preview");

    if (elIcon.value.startsWith("http"))
    {
        elPreview.style.display = "none";
        elImgPreview.style.display = "block";
        elImgPreview.src = elIcon.value;
    }
    else
    {
        elPreview.className = "fa-2x fas fa-"+elIcon.value;
        elPreview.style.color = colorPicker.getColor().toHEX().toString();
        elPreview.style.display = "block";
        elImgPreview.style.display = "none";
    }
}

function copyToREADMEClipboard()
{
    var elem = document.getElementById("rawREADME");

    elem.select();
    document.execCommand('copy');
    elem.style.backgroundColor = "#000";
    elem.setSelectionRange(0,0);
    elem.style.backgroundColor = "#FFF";
}

function initializeColorPicker(elSelector,defaultColorHex,onChangeCallback){
    return new Pickr({
        el: elSelector,
        default: defaultColorHex,
    comparison: false,
        components: {
            preview: true,
            opacity: false,
            hue: true,
            interaction: {
                hex: true,
                rgba: true,
                hsva: true,
                input: true,
                clear: false,
                save: false
            }
        },
        onChange(hsva, instance) {
            onChangeCallback();
        },
        onSave(hsva, instance) {
            onChangeCallback();
        }
    });
}

function initialize() {
    var evt = [];
    evt.currentTarget = document.getElementById("Intro");
    toTab(evt);
    colorPicker = initializeColorPicker('#icon_color','#40DBB0',update_icon);
}

</script>


</head>


<body onload="initialize();">
    <div class="topnav">
        <img class="logo" src="mycroft.svg" height="24px" />
        <!-- | Skills -->
    </div>

    <div class="tab">
      <button id="Intro"     class="tablinks" onclick="toTab(event)">Intro</button>
      <button id="Edit"      class="tablinks" onclick="toTab(event)"><i class="fas fa-edit" style="color:#22a7f0;"></i> Edit</button>
      <button id="Preview"   class="tablinks" onclick="generateREADME(); generatePreview(); toTab(event)"><i class="fas fa-cogs" style="color:#40DBB0;"></i> Github Preview</button>
      <button id="PreviewCard" class="tablinks" onclick="generatePreviewCard(); generatePreview(); toTab(event)"><i class="fas fa-cogs" style="color:#40DBB0;"></i> Card Preview</button>
      <button id="PreviewDetail" class="tablinks" onclick="generatePreviewDetail(); generatePreview(); toTab(event)"><i class="fas fa-cogs" style="color:#40DBB0;"></i> Details Preview</button>
      <button id="README"    class="tablinks" onclick="generateREADME(); toTab(event)"><i class="fas fa-copy" style="color:#FD9E66;"></i> README.md</button>
    </div>

    <div id="page_Intro" class="tabcontent">
        <h1>Mycroft Skill Readme Generator</h1>
        <p>This tool generates a README.md for your Mycroft Skill repository on GitHub. It will be machine-parsed to fill the Mycroft Skill Marketplace and will explain your Skill to users in a standardized, easy to read format.</p>

        <div class="instructions">
            <h2>How it works</h2>
            <i class="fas fa-edit" style="color:#22a7f0;"></i> Edit the form<br/>
            <i class="fas fa-cogs" style="color:#40DBB0;"></i> Generate and examine previews<br/>
      <i class="fas fa-copy" style="color:#FD9E66;"></i> Copy the output into a README.md file for your Skill's repo<br/>
      <h2>optionally</h2>
            <i class="fas fa-paste" style="color:purple;"></i> Edit or Paste an existing README.md in the README tab.<br/>
        </div>

        <div id="community-links" class="instructions">
            <p>
                <a href="https://mycroft.ai/documentation/">Documentation</a> is also available on writing Skills for Mycroft, and you are welcome to join the <a href="https://chat.mycroft.ai/community/channels/skills">Skills development Chat channel</a>, where you can liaise with other Skill Authors and request assistance.
            </p>
        </div>
    </div>

    <div id="page_Edit" class="tabcontent">

        <form class="entry-form">
            <ul>

                <li>
                    <label for="name">Name</label>
                    <input type="text" id="name" maxlength="100" onkeyup="generate()" placeholder="Your skill name"/>
                    <span>Brief, speakable skill name.  Capitalize most words.  Ex: "Podcast Player".<br/>NOTE: Avoid the word "Skill" in the name.</span>
                </li>

                <li>
                    <label for="icon">Icon</label>
                    <div>
                        <table width="100%" style="margin-left: 20px">
                        <tr>
                            <td style="vertical-align:top">Preview:<br/><i id="icon_preview" class="fa-2x fas fa-robot" style="color:#40DBB0;"></i><img id="img_preview" src="" width="41" height="41" style="display:none;"/></td>
                            <td width="70%">Font Awesome Name / or image URL:<input type="text" id="icon" maxlength="255" placeholder="robot" value="robot" onkeyup="update_icon()"/></td>
                            <td>Color:<br/>
                                <div id="icon_color"></div>
                            </td>
                        </table>
                    </div>
                    <span>Go to <a href="https://fontawesome.com/cheatsheet" target="_blank">Font Awesome</a>,
                    pick a free  icon and copy its name here (eg. 'paw'), along with a <a href="https://mycroft.ai/colors" target="_blank">color</a>.  Alternately, provide a full URL to your 50x50 icon image (.png or .jpg only).</span>
                </li>

                <li>
                    <label for="short_desc">One-line Description</label>
                    <input type="text" id="short_desc" "=" maxlength="100" placeholder="Brief one line description"/>
                    <span>Enter a one-line description of your skill. Ex: "Play and subscribe to podcasts"</span>
                </li>

                <li>
                    <label for="long_desc">Long Description</label>
                    <textarea id="long_desc" onkeyup="adjust_textarea(this)" placeholder="Full, multi-paragraph description..."></textarea>
                    <span>Free form, multi-paragraph description of the Skill. You can use <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Github markdown</a>.</span>
                </li>

                <li id="all_ex">
                    <label for="ex_1">User Phrases: Hey Mycroft...</label>
                    <input class="ex" type="text" id="ex_1" maxlength="100" placeholder="Phrase 1" onkeyup="addNext(this, 'ex_')"/>
                    <span>Provide examples of phrases handled by the Skill after the Wake Word is spoken. The first may be highlighted and should be a prime example.<br/>Ex: "play the news", "set a 10-minute timer"</span>
                </li>

                <li id="all_authors">
                    <label for="author_1">Author(s)</label>
                    <input class="author" type="text" id="author_1" maxlength="100" placeholder="Author name (@github_handle) 1" onkeyup="addNext(this, 'author_')"/>
                    <span>Credits for people or organizations involved (name, email, and/or GitHub @handle).</span>
                </li>

                <li>
                    <label>Supported Devices</label>

                        <div class="device first"><input type="radio" id="support_all" name="supported" onchange="checkAllDevices()" checked="true" value="all"/>
                            <label for="support_all">All Devices (no specific requirements)</label></div>

                        <div class="device first"><input type="radio" id="support_specific" name="supported" value="specific"/>
                            <label for="support_specific">Specific devices</label>

                            <div class="device"><input type="checkbox" id="req_mark1" onchange="checkDevices()" value="mark1"/>
                                <label for="req_mark1">Platform: Mark I</label></div>
                            <div class="device"><input type="checkbox" id="req_mark2" onchange="checkDevices()" value="mark2"/>
                                <label for="req_mark2">Platform: Mark II</label></div>
                            <div class="device"><input type="checkbox" id="req_picroft" onchange="checkDevices()" value="picroft"/>
                                <label for="req_picroft">Platform: Picroft</label></div>
                            <div class="device"><input type="checkbox" id="req_plasmoid" onchange="checkDevices()" value="plasmoid"/>
                                <label for="req_plasmoid">Platform: KDE Plasmoid</label></div>
                        </div>

                    <span>If only for specific platforms, check one or more (blank means any platform).</span>
                </li>

                <li>
                    <label>Category</label>

                    <div class="category first"><input class="category_section" type="checkbox" onclick='categoryClick(this);' id="cat_Daily" value="Daily"/>
                        <label for="cat_Daily" id="for_cat_Daily"><span>Daily</span> &mdash; time, alarms, timers, and weather</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' id="cat_Configuration" value="Configuration"/>
                        <label for="cat_Configuration" id="for_cat_Configuration"><span>Configuration</span> &mdash; query and change account or device settings</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' id="cat_Entertainment" value="Entertainment"/>
                        <label for="cat_Entertainment" id="for_cat_Entertainment"><span>Entertainment</span> &mdash; jokes, sport scores, games</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' id="cat_Information" value="Information"/>
                        <label for="cat_Information" id="for_cat_Information"><span>Information</span> &mdash; stocks, quotes, general knowledge</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' id="cat_IoT" value="IoT"/>
                        <label for="cat_IoT" id="for_cat_IoT"><span>IoT</span> &mdash; home automation, lighting controlling</label></div>

                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' name="category" id="cat_Music" value="Music"/>
                        <label for="cat_Music" id="for_cat_Music"><span>Music & Audio</span> &mdash; listen to streaming services</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);' name="category" id="cat_Media" value="Media"/>
                        <label for="cat_Media" id="for_cat_Media"><span>Media</span> &mdash; controlling video streamer, stereo</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);'  name="category" id="cat_Productivity" value="Productivity"/>
                        <label for="cat_Productivity" id="for_cat_Productivity"><span>Productivity</span> &mdash; mail, calendar, Pomodoro</label></div>
                    <div class="category"><input class="category_section" type="checkbox" onclick='categoryClick(this);'  name="category" id="cat_Transport" value="Transport"/>
                        <label for="cat_Transport" id="for_cat_Transport"><span>Transport</span> &mdash; bus/train schedules, ride services</label></div>

                    <span>The first Category selected will be bold as the Primary Category for display, all others are secondary for searches.</span>
                </li>

                <li id="all_tags">
                    <label for="tag_1">Tags</label>
                    <input class="tag" type="text" id="tag_1" maxlength="100" placeholder="#Tag 1" onkeyup="addNext(this, 'tag_')" onchange="validateTag(this)"/>
                    <span>Tags are single word identifiers, such as #kids, #crypto and are used for searching.</span>
        </li>

                <li>
                    <label for="custom_section">Custom Sections</label>
                    <textarea id="custom_sections" onkeyup="adjust_textarea(this)" placeholder=
"## Your own section title
Markdown text

##Another section
Yadda yadda..."></textarea>
                    <span><b>Optional:</b>  You can add one or more custom sections to be included in your readme.  These won't appear inside the Marketplace, but can describe any information another developer might be interested.  History, how to build associate hardware, references to other projects ...  just use regular </b> <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Github markdown</a>.</span>
                </li>
            </ul>

            For help, see the ~skills channel at <a href="https://chat.mycroft.ai/community/channels/skills">https://chat.mycroft.ai</a>.
        </form>
    </div>


    <div id="page_Preview" class="tabcontent">
        <p>Below is a preview of how the README.md will look in your Skill's Github repo.</p>
            <iframe id="github_preview_frame" class="markdown-body">abc</iframe>
        <div id="github_preview" class="markdown-body">
        </div>
    </div>

    <div id="page_PreviewCard" class="tabcontent">
        <p>Below is a preview of a small reference card.</p>
        <div><span id="card_small_category">Tester</span></div>
        <div id="card_small_preview" class="card">
            <div class="card_content">
                <div style="width: 100%;"><i id="icon_small" class="fa-2x fas fa-comment" style="color:#22a7f0; text-align: center;"></i></div>
                <div><img id="img_icon_small" src="" width="45" height="45" style="display:none"/> <span id="title_small">Coin Flip</span></div>

                <div id="utt_small"><i class="fas fa-comment" style="color:#22a7f0;"></i>&nbsp;<span id="utt_0_small">testing</span></div>

                <div><span id="desc_small">This is a shortish description for the Skill</span></div>

                <div><input type="button" value="Install"/></div>
            </div>
        </div>
    </div>

    <div id="page_PreviewDetail" class="tabcontent">
        <p>Below is a preview of a large reference card.</p>
        <div id="cardb_large_preview" class="card">
            <div class="card_content">
                <div id="cardb_large_title">
                <div><i id="icon_large" class="fa-2x fas fa-comment" style="color:#22a7f0;"></i><img id="img_icon_large" src="" width="45" height="45" style="display:none"/> <span id="title_large">Coin Flip</span></div>
                <span id="desc_large">This is a shortish description for the Skill</span>
                </div>

                <div id="utt_large_1"><i class="fas fa-comment" style="color:#22a7f0;"></i>&nbsp;<span id="utt_1_large">testing</span></div>

                <div id="div_fulldesc_large"><span id="fulldesc_large">This is the full description for the Skill</span></div>

                <div id="by_large"><b>Credits:</b><br/><span id="author_large">By whoever (@whoever)</span></div>

                <div><input type="button" value="Install"/></div>
            </div>
        </div>
    </div>

    <div id="page_README" class="tabcontent">
        <p>Below is the basis of the README.md for your Skill's Github repo.  You can safely extend the contents with a custom sections below the generated content, such as <tt>## Notes</tt> or <tt>## TODO</tt>. But refrain from changing the format or order of the generated content to ensure compatibility with parsers.</p>
        <p><b>README.md</b>
          <input type="button" onclick="copyToREADMEClipboard()" value="Copy to Clipboard">
          <span id="msgImportedREADME" style="display: none">changes applied</span><br/>
          <textarea id="rawREADME" placeholder="Fill the above form and hit Generate." onchange="parseREADME()" oninput="showREADMEImport()"></textarea>
          <span id="lblREADMENote">NOTE: Edits made here will be applied back to the edit form and previews.  Be aware that non-standard README features can be lost in the round-trip after you leave this page.</span>
        </p>
    </div>
</body>

<span class="gr__tooltip">
    <span class="gr__tooltip-content"></span>
<i class="gr__tooltip-logo"></i>
<span class="gr__triangle"></span>
</span>

</html>
