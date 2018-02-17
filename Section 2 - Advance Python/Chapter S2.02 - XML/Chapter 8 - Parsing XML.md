
# Parsing XML in Python

Original url: https://github.com/mikekestemont/ghent1516/blob/master/Chapter%208%20-%20Parsing%20XML.ipynb

## XML in a nutshell

So far, we have primarily dealt with unstructured data in this course: we have learned to read, for example, the contents of plain text files in the previous chapters. Such raw textual data is often called 'unstructured', because it lacks annotations that make explicit the function or meaning of the words in the documents. If we read the contents of a play as a plain text, for instance, we don't have a clue to which scene or act a particular utterance belongs, or by which character the utterance was made. Nowadays, it is therefore increasingly common to add annotations to a text that give us a better insight into the
semantics and structure of the data. Adding annotations to texts (e.g. scholarly editions of Shakepeare), is typically done using some form of markup. Various markup-languages exist that allow us to provide structured and unambiguous annotations to a (digital) text. XML or the "eXtensible Mark-up Language" is currently one of the dominant standards to encode texts in the Digital Humanities. In this chapter, we'll assume that have at least some notion of XML, although we will have a quick refresher below. XML is a pretty straightforward mark-up language: let's have a look at Shakepeare's well-known sonnet 18 encoded in XML (you can find this poem also as `sonnet.txt` in your `data/TEI` folder).

<?xml version="1.0"?>
<sonnet author="William Shakepeare" year="1609">
<line n="1">Shall I compare thee to a summer's <rhyme>day</rhyme>?</line>
	<line n="2">Thou art more lovely and more <rhyme>temperate</rhyme>:</line>
    <line n="3">Rough winds do shake the darling buds of <rhyme>May</rhyme><break n="3"/>,</line>
	<line n="4">And summer's lease hath all too short a <rhyme>date</rhyme>:</line>
	<line n="5">Sometime too hot the eye of heaven <rhyme>shines</rhyme>,</line>
	<line n="6">And often is his gold complexion <rhyme>dimm'd</rhyme>;</line>
	<line n="7">And every fair from fair sometime <rhyme>declines</rhyme>,</line>
	<line n="8">By chance, or nature's changing course, <rhyme>untrimm'd</rhyme>;</line>
    <volta/>
	<line n="9">But thy eternal summer shall not <rhyme>fade</rhyme></line>
	<line n="10">Nor lose possession of that fair thou <rhyme>ow'st</rhyme>;</line>
	<line n="11">Nor shall Death brag thou wander'st in his <rhyme>shade</rhyme>,</line>
	<line n="12">When in eternal lines to time thou <rhyme>grow'st</rhyme>;</line>
	<line n="13">So long as men can breathe or eyes can <rhyme>see</rhyme>,</line>
	<line n="14">So long lives this, and this gives life to <rhyme>thee</rhyme>.</line>
</sonnet>

The first line in our Shakespearean example (<?xml version="1.0"?>) declares which exact version of XML we are using, in our case version 1. As you can see at a glance, XML typically encodes pieces of text using *start tags* (e.g. `<line>, <rhyme>`) and *end tags* (`</line>`, `</rhyme>`). Each start tag must correspond to exactly one end tag, although XML does allow for "solo" elements such the `<volta/>` tag after line 8 in this example. Interestingly, XML tag are not allowed to overlap. The following line would therefore not constitue valid XML:

<line><sentence>This is a </line><line>sentence.</sentence></line>

The following two lines would be valid alternatives for this example, because here the tags don't overlap:

<sentence><line>This is a </line><line>sentence.</line></sentence>
<sentence>This is a <linebreak/>sentence.</sentence>

This limitation has to with the fact that XML is a *hierarchical* markup language: it assumes that we can describe a text document as a tree of branching nodes. In this tree, elements cannot have more than one direct parent element (otherwise the hearchy would be ambiguous). The one exception is the so-called root element, which as the highest node in tree does not have a parent element itself. Logically speaking, all this entails that a valid XML document can only have a single *root element*. Note that all non-root elements can have as many siblings as we wish. All the `<line>` elements in our sonnet, for example, are siblings, in the sense that they have in common a direct parent element, i.e. the <sonnet> tag. Finally, note that we can add extra information to our elements using so-called attributes. The `n` attribute, for example, give us the line number for each line in the sonnet, surrounded by double quotation marks. The <sonnet> element illlustrates that we can add as many attributes as we want to a tag. 

## XML and Python

Researchers in the Digital Humanities nowadays often put a lot of time and effort in creating digital data sets for their research, such as scholarly editions with a rich markup encoded in XML. Nevertheless, once this data has been annotated, it can be tricky to get your texts out again, so to speak, and fully exploit the information which you painstakingly encoded. Therefore, it is crucial to be able to parse XML in an efficient manner. Luckily, Python provides all the tools necessary to do this. We will make use of the `lxml` library, which is part of the Anaconda Python distribution: 


```python
from lxml import etree
```

For the record, we should mention that there exist many other libraries in Python to parse XML, such as `minidom` or `BeautifulSoup` which is an interesting library, when you intend to scrape data from the web. While these might come with more advanced bells and whistles than `lxml`, they can also be more complex to use, which is why we stick to `lxml` in this course. Let us now import our sonnet in Python, which has been saved in the file `sonnet18.xml`:


```python
tree = etree.parse("data/books.xml")
print(tree)
```

    <lxml.etree._ElementTree object at 0x000001D77D0B0208>


Python has now read and parsed our xml-file via the `etree.parse()` function. We have stored our XML tree structure, which is returned by the `parse()` function, in the `tree` variable, so that we can access it later. If we print `tree` as such, we don't get a lot of useful information. To have a closer look at the XML in a printable text version, we need to call the `tostring()` method on the `tree` before printing it.


```python
print(etree.tostring(tree))
```

    b'<catalog>\n   <book id="bk101">\n      <author>Gambardella, Matthew</author>\n      <title>XML Developer\'s Guide</title>\n      <genre>Computer</genre>\n      <price>44.95</price>\n      <publish_date>2000-10-01</publish_date>\n      <description>An in-depth look at creating applications \n      with XML.</description>\n   </book>\n   <book id="bk102">\n      <author>Ralls, Kim</author>\n      <title>Midnight Rain</title>\n      <genre>Fantasy</genre>\n      <price>5.95</price>\n      <publish_date>2000-12-16</publish_date>\n      <description>A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.</description>\n   </book>\n   <book id="bk103">\n      <author>Corets, Eva</author>\n      <title>Maeve Ascendant</title>\n      <genre>Fantasy</genre>\n      <price>5.95</price>\n      <publish_date>2000-11-17</publish_date>\n      <description>After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.</description>\n   </book>\n   <book id="bk104">\n      <author>Corets, Eva</author>\n      <title>Oberon\'s Legacy</title>\n      <genre>Fantasy</genre>\n      <price>5.95</price>\n      <publish_date>2001-03-10</publish_date>\n      <description>In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.</description>\n   </book>\n   <book id="bk105">\n      <author>Corets, Eva</author>\n      <title>The Sundered Grail</title>\n      <genre>Fantasy</genre>\n      <price>5.95</price>\n      <publish_date>2001-09-10</publish_date>\n      <description>The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon\'s Legacy.</description>\n   </book>\n   <book id="bk106">\n      <author>Randall, Cynthia</author>\n      <title>Lover Birds</title>\n      <genre>Romance</genre>\n      <price>4.95</price>\n      <publish_date>2000-09-02</publish_date>\n      <description>When Carla meets Paul at an ornithology \n      conference, tempers fly as feathers get ruffled.</description>\n   </book>\n   <book id="bk107">\n      <author>Thurman, Paula</author>\n      <title>Splish Splash</title>\n      <genre>Romance</genre>\n      <price>4.95</price>\n      <publish_date>2000-11-02</publish_date>\n      <description>A deep sea diver finds true love twenty \n      thousand leagues beneath the sea.</description>\n   </book>\n   <book id="bk108">\n      <author>Knorr, Stefan</author>\n      <title>Creepy Crawlies</title>\n      <genre>Horror</genre>\n      <price>4.95</price>\n      <publish_date>2000-12-06</publish_date>\n      <description>An anthology of horror stories about roaches,\n      centipedes, scorpions  and other insects.</description>\n   </book>\n   <book id="bk109">\n      <author>Kress, Peter</author>\n      <title>Paradox Lost</title>\n      <genre>Science Fiction</genre>\n      <price>6.95</price>\n      <publish_date>2000-11-02</publish_date>\n      <description>After an inadvertant trip through a Heisenberg\n      Uncertainty Device, James Salway discovers the problems \n      of being quantum.</description>\n   </book>\n   <book id="bk110">\n      <author>O\'Brien, Tim</author>\n      <title>Microsoft .NET: The Programming Bible</title>\n      <genre>Computer</genre>\n      <price>36.95</price>\n      <publish_date>2000-12-09</publish_date>\n      <description>Microsoft\'s .NET initiative is explored in \n      detail in this deep programmer\'s reference.</description>\n   </book>\n   <book id="bk111">\n      <author>O\'Brien, Tim</author>\n      <title>MSXML3: A Comprehensive Guide</title>\n      <genre>Computer</genre>\n      <price>36.95</price>\n      <publish_date>2000-12-01</publish_date>\n      <description>The Microsoft MSXML3 parser is covered in \n      detail, with attention to XML DOM interfaces, XSLT processing, \n      SAX and more.</description>\n   </book>\n   <book id="bk112">\n      <author>Galos, Mike</author>\n      <title>Visual Studio 7: A Comprehensive Guide</title>\n      <genre>Computer</genre>\n      <price>49.95</price>\n      <publish_date>2001-04-16</publish_date>\n      <description>Microsoft Visual Studio 7 is explored in depth,\n      looking at how Visual Basic, Visual C++, C#, and ASP+ are \n      integrated into a comprehensive development \n      environment.</description>\n   </book>\n</catalog>'


You'll notice that we actually get a string in a raw format: if we want to display it properly, we have to decode it:


```python
print(etree.tostring(tree).decode())
```

    <catalog>
       <book id="bk101">
          <author>Gambardella, Matthew</author>
          <title>XML Developer's Guide</title>
          <genre>Computer</genre>
          <price>44.95</price>
          <publish_date>2000-10-01</publish_date>
          <description>An in-depth look at creating applications 
          with XML.</description>
       </book>
       <book id="bk102">
          <author>Ralls, Kim</author>
          <title>Midnight Rain</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-12-16</publish_date>
          <description>A former architect battles corporate zombies, 
          an evil sorceress, and her own childhood to become queen 
          of the world.</description>
       </book>
       <book id="bk103">
          <author>Corets, Eva</author>
          <title>Maeve Ascendant</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2000-11-17</publish_date>
          <description>After the collapse of a nanotechnology 
          society in England, the young survivors lay the 
          foundation for a new society.</description>
       </book>
       <book id="bk104">
          <author>Corets, Eva</author>
          <title>Oberon's Legacy</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2001-03-10</publish_date>
          <description>In post-apocalypse England, the mysterious 
          agent known only as Oberon helps to create a new life 
          for the inhabitants of London. Sequel to Maeve 
          Ascendant.</description>
       </book>
       <book id="bk105">
          <author>Corets, Eva</author>
          <title>The Sundered Grail</title>
          <genre>Fantasy</genre>
          <price>5.95</price>
          <publish_date>2001-09-10</publish_date>
          <description>The two daughters of Maeve, half-sisters, 
          battle one another for control of England. Sequel to 
          Oberon's Legacy.</description>
       </book>
       <book id="bk106">
          <author>Randall, Cynthia</author>
          <title>Lover Birds</title>
          <genre>Romance</genre>
          <price>4.95</price>
          <publish_date>2000-09-02</publish_date>
          <description>When Carla meets Paul at an ornithology 
          conference, tempers fly as feathers get ruffled.</description>
       </book>
       <book id="bk107">
          <author>Thurman, Paula</author>
          <title>Splish Splash</title>
          <genre>Romance</genre>
          <price>4.95</price>
          <publish_date>2000-11-02</publish_date>
          <description>A deep sea diver finds true love twenty 
          thousand leagues beneath the sea.</description>
       </book>
       <book id="bk108">
          <author>Knorr, Stefan</author>
          <title>Creepy Crawlies</title>
          <genre>Horror</genre>
          <price>4.95</price>
          <publish_date>2000-12-06</publish_date>
          <description>An anthology of horror stories about roaches,
          centipedes, scorpions  and other insects.</description>
       </book>
       <book id="bk109">
          <author>Kress, Peter</author>
          <title>Paradox Lost</title>
          <genre>Science Fiction</genre>
          <price>6.95</price>
          <publish_date>2000-11-02</publish_date>
          <description>After an inadvertant trip through a Heisenberg
          Uncertainty Device, James Salway discovers the problems 
          of being quantum.</description>
       </book>
       <book id="bk110">
          <author>O'Brien, Tim</author>
          <title>Microsoft .NET: The Programming Bible</title>
          <genre>Computer</genre>
          <price>36.95</price>
          <publish_date>2000-12-09</publish_date>
          <description>Microsoft's .NET initiative is explored in 
          detail in this deep programmer's reference.</description>
       </book>
       <book id="bk111">
          <author>O'Brien, Tim</author>
          <title>MSXML3: A Comprehensive Guide</title>
          <genre>Computer</genre>
          <price>36.95</price>
          <publish_date>2000-12-01</publish_date>
          <description>The Microsoft MSXML3 parser is covered in 
          detail, with attention to XML DOM interfaces, XSLT processing, 
          SAX and more.</description>
       </book>
       <book id="bk112">
          <author>Galos, Mike</author>
          <title>Visual Studio 7: A Comprehensive Guide</title>
          <genre>Computer</genre>
          <price>49.95</price>
          <publish_date>2001-04-16</publish_date>
          <description>Microsoft Visual Studio 7 is explored in depth,
          looking at how Visual Basic, Visual C++, C#, and ASP+ are 
          integrated into a comprehensive development 
          environment.</description>
       </book>
    </catalog>


If we have more complex data, it might also be to set the `pretty_print` parameter to `True`, to obtain a more beautifully formatted string, with Python taking care of indendation etc. In our example, it doesn't change much:


```python
print(etree.tostring(tree, pretty_print=True).decode())
```

Now let us start processing the contents of our file. Suppose that we are not really interested in the full hierarchical structure of our file, but just in the rhyme words occuring in it. The high-level function `interfind()` allows us to easily select all `rhyme`-element in our tree, regardless of where exactly they occur. Because this functions returns a list of nodes, we can simply loop over them:


```python
print(len(list(tree.iterfind("//book"))))
for node in tree.iterfind("//book"):
    print(node)
```

    13
    <Element book at 0x1d77d0be988>
    <Element book at 0x1d77d0be948>
    <Element book at 0x1d77d0a7688>
    <Element book at 0x1d77d0be988>
    <Element book at 0x1d77d0be948>
    <Element book at 0x1d77d0a7688>
    <Element book at 0x1d77d0be988>
    <Element book at 0x1d77d0be948>
    <Element book at 0x1d77d0a7688>
    <Element book at 0x1d77d0be988>
    <Element book at 0x1d77d0be948>
    <Element book at 0x1d77d0a7688>
    <Element book at 0x1d77d0be988>


Note that the search expression (`"//rhyme"`) has two forward slashes before our actual search term. This is in fact XPath syntax, and the two slashes indicate that the search term can occur anywhere (e.g. not necessarily among a node's direct children). Unfortunately, printing the nodes themselves again isn't really insightful: in this way, we only get rather prosaic information of the Python objects holding our `rhyme` nodes. We can use the `.tag` property to print the tag's name:


```python
print(len(list(tree.iterfind("/catalog"))))
for node in tree.iterfind("/catalog/book"):
    print(node)
```

    0



```python
for node in tree.iterfind("/book"):
    print(node.tag)
```

    book
    book
    book
    book
    book
    book
    book
    book
    book
    book
    book
    book


To extract the actual rhyme word contained in the element, we can use the `.text` property of the nodes:


```python
for node in tree.iterfind("//book"):
    print(node.text)
```

    
          
    newbook2
    
          
    
          
    
          
    
          
    
          
    
          
    
          
    
          
    
          
    
          
    
          


That looks better!

Just now, we have been iterating over our `rhyme` elements in simple order of appearance: we haven't been really been exploiting the hierarchy of our XML file yet. Let's see now how we can navigate our xml tree. Let's first select our root node: there's a function for that!


```python
root_node = tree.getroot()
print(root_node.tag)
```

We can access the value of the attributes of an element via `.attrib`, just like we would access the information in a Python dictionary, that is via key-based indexing. We know that our `sonnet` element, for instance, should have an `author` and `year` attribute. We can inspect the value of these as follows:


```python
print(root_node.attrib["author"])
print(root_node.attrib["year"])
```

If we wouldn't know which attributes were in fact available for a node, we could also retrieve the attribute names by calling `keys()` on the `attributes` property of a node, just like we would do with a regular dictionary: 


```python
for key in root_node.attrib.keys():
    print(root_node.attrib[key])
```

So far so good. Now that we have selected our root element, we can start drilling down our tree's structure. Let us first find out how many child nodes our root element has: 


```python
print(len(root_node))
```

Our root node turns out to have 15 child nodes, which makes a lot of sense, since we have 14 `line` elements and the `volta`. We can actually loop over these children, just as we would loop over any other list:


```python
for node in root_node:
    print(node.tag)
```

To extract the actual text in our lines, we need one additional `for`-loop which will allow us to iteratre over the pieces of text under each line:


```python
for node in root_node:
    if node.tag != "volta":
        line_text = ""
        for text in node.itertext():
            line_text = line_text + text
        print(line_text)
    else:
        print("=== Volta found! ===")
```

Note that we get an empty line at the `volta`, since there isn't any actual text associated with this empty tag.

### Quiz!
Could you now write your own code, which iterates over the lines in our tree and prints out the line number based on the `n` attribute of the `line` element?


```python
for node in root_node:
    if node.tag == "line":
        print(node.attrib["n"])
```

## Manipulating XML in Python

So far, we have parsed XML in Python, we haven't dealt with creating or manipulating XML in Python. Luckily, adapting or creating XML is fairly straightforward in Python. Let's first try and change the author's name in the `author` attribute of the `sonnet`. Because this boils down to manipulating a Python dictionary, the syntax should already be familiar to you: 


```python
root_node = tree.getroot()
root_node.attrib["author"] = "J.K. Rowling"
root_node.attrib["year"] = "2015"
root_node.attrib["new_element"] = "dummy string!"
root_node.attrib["place"] = "maynooth"
print(etree.tostring(root_node).decode())
```

That was easy, wasn't it? Did you see we can just add new attributes to an element? Just take care only to put strings as attribute values: since we are working with XML, Python won't accept e.g. numbers and you will get an error:


```python
root_node.attrib["year"] = "2015"
```

Adding whole elements is fairly easy too. Let's add a single dummy element (`<break/>`) to indicate a line break at the end of each line. Importantly, we have to create this element inside our loop, before we can add it:


```python
break_el = etree.Element("break")
break_el.attrib["author"] = "Mike"
print(etree.tostring(break_el).decode())
```

You'll notice that we actually created an empty `<break/>` tag. Now, let's add it add the end of each line:


```python
for node in tree.iterfind("//line"):
    break_el = etree.Element("break")
    node.append(break_el)
print(etree.tostring(tree).decode())
```

Adding an element with actual content is just as easy by the way:


```python
break_el = etree.Element("break")
print(etree.tostring(break_el).decode())
break_el.text = "XXX"
print(etree.tostring(break_el).decode())
```

### Quiz
The `<break/>` element is still empty: could you add to it an `n` attribute, to which you assign the line number from the current <line> element?


```python
tree = etree.parse("data/TEI/sonnet18.xml")
root_node = tree.getroot()
for node in root_node:
    if node.tag == "line":
        v = node.attrib["n"]
        break_el = etree.Element("break")
        break_el.attrib["n"] = v
        node.append(break_el)
print(etree.tostring(tree).decode())
```

## Python for TEI

In Digital Humanities, you hear a lot about the TEI nowadays, or the Text Encoding Initiative ([tei-c.org](http://www.tei-c.org/index.xml)). The TEI refers to an initiative which has developed a highly influential "dialect" of XML for encoding texts in the Humanities. The beauty about XML is that tag names aren't predefined and you can invent your own tag and attributes. Our Shakepearean example could just have well have read:

<?xml version="1.0"?>
<poem writer="William Shakepeare" date="1609">
	<l nr="1">Shall I compare thee to a summer's <last>day</last>?</l>
	<l nr="2">Thou art more lovely and more <last>temperate</last>:</l>
	<l nr="3">Rough winds do shake the darling buds of <last>May</last>,</l>
	<l nr="4">And summer's lease hath all too short a <last>date</last>:</l>
	<l nr="5">Sometime too hot the eye of heaven <last>shines</last>,</l>
	<l nr="6">And often is his gold complexion <last>dimm'd</last>;</l>
	<l nr="7">And every fair from fair sometime <last>declines</last>,</l>
	<l nr="8">By chance, or nature's changing course, <last>untrimm'd</last>;</l>
    <break/>
	<l nr="9">But thy eternal summer shall not <last>fade</last></l>
	<l nr="10">Nor lose possession of that fair thou <last>ow'st</last>;</l>
	<l nr="11">Nor shall Death brag thou wander'st in his <last>shade</last>,</l>
	<l nr="12">When in eternal lines to time thou <last>grow'st</last>;</l>
	<l nr="13">So long as men can breathe or eyes can <last>see</last>,</l>
	<l nr="14">So long lives this, and this gives life to <last>thee</last>.</l>
</poem>

As you can see, all the tag and attribute names are different in this version, but the essential structure is still the same. You could therefore say that XML is a markup language which provides a *syntax* to talk about texts, but does not come with a default *semantics*. This freedom in choosing name tags etc. can also be a bit daunting: this is why the TEI provides Guidelines as how tag names etc. can be used to mark up specific phenomena in texts. The TEI therefore also refers to a rather bulky set of guidelines as to which tags could be used to properly encode a text. Below, we read in a fairly advanced example of Shakepeare's 17th sonnet encoded in TEI (note the use of the `<TEI>` tag as our root node!). Even the metrical structure has been encoded as you will see, so this can be considered an example "TEI on steroids". 


```python
tree = etree.parse("data/TEI/sonnet17.xml")
print(etree.tostring(tree).decode())
```

## Quiz

Processing TEI in Python, is really just processing XML in Python, the dark art which you already learned to master above! Let's try and practice the looping techniques we introduced above. Could you provide code which parses the xml and writes away the lines in this poem to a plain text file, with one verse line on a single line in the new file?


```python
# add your parsing code here... 
```

## A hands-on case study: French plays

OK, it time to get your hands even more dirty. For textual analyses, there are a number of great datasets out there which have been encoded in rich XML. One excellent resource which we have recently worked with, can be found at [theatre-classique.fr](http://www.theatre-classique.fr/): this website holds an extensive collection of French plays from the time of the Classical and Enlightenment era in France. Some of the plays have been authored by some of France's finest authors such as Molière pr Pierre and Thomas Corneille. What is interesting about this resource, is that it provides a very rich XML markup: apart from extensive metadata on the play or a detailed descriptions of the actors involved, the actually lines have been encoded in such a manner, that we perfectly know which character uttered a particular line, or to which scene or act a line belongs. This allows us to perform much richer textual analyses than if we would only have a raw text version of the plays. We have collected a subset of these plays for you under the `data/TEI`directory:


```python
import os
dirname = "data/TEI/french_plays/"
for filename in os.listdir(dirname):
    if filename.endswith(".xml"):
        print(filename)
```

OK: under this directory, we appear to have a bunch of XML-files, but their titles are just numbers, which doesn't tell us a lot. Let's have a look at what's the title and author tags in these files:


```python
for filename in os.listdir(dirname):
    if filename.endswith(".xml"):
        print("*****")
        print("\t-", filename)
        tree = etree.parse(dirname+filename)
        author_element = tree.find("//author") # find vs iterfind!
        print("\t-", author_element.text)
        title_element = tree.find("//title")
        print("\t-", title_element.text)
```

As you can see, we have made you a nice subset selection of this data, containing only texts by the famous pair of brothers: Pierre and Thomas Corneille. We have provided a number of exercises in which you can practice your newly developed XML skills. In each of the fun little tasks below, you should compare the dramas of our two famous brothers:
* how many characters does each brother on average stage in a play?
* which brother has the highest vocabulary richness?
* which brother uses the lengthiest speeches per character on average?
* which brother gives most "speech time" to women, expressed in number of words (hint: you can derive a character's gender from the `<castList>` in most plays!)


```python
# your code goes here
```

------------------------


```python
# from IPython.core.display import HTML
# def css_styling():
#     styles = open("styles/custom.css", "r").read()
#     return HTML(styles)
# css_styling()
```
