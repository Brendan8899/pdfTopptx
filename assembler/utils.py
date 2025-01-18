
from pptx.oxml.xmlchemy import OxmlElement

def SubElement(parent, tagname, **kwargs):
        element = OxmlElement(tagname)
        element.attrib.update(kwargs)
        parent.append(element)
        return element
    
def makeParaBulletPointed(para):
    """Bullets are set to Arial,
        actual text can be a different font"""
    pPr = para._p.get_or_add_pPr()
    ## Set marL and indent attributes
    pPr.set('marL','171450')
    pPr.set('indent','171450')
    ## Add buFont
    _ = SubElement(parent=pPr,
                   tagname="a:buFont",
                   typeface="Arial",
                   panose="020B0604020202020204",
                   pitchFamily="34",
                   charset="0"
                   )
    ## Add buChar
    _ = SubElement(parent=pPr,
                   tagname='a:buChar',
                   char="•")
    