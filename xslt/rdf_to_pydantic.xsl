<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:skos="http://www.w3.org/2004/02/skos/core#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:my="http://myfuctions"
    exclude-result-prefixes="#all"
    expand-text="yes">
    
    <xsl:output method="text" indent="no"/>
    
    <xsl:function name="my:toCamelCase" as="xs:string">
        <xsl:param name="input" as="xs:string"/>
        <xsl:variable name="words" select="tokenize($input, ' ')"/>
        <xsl:value-of select="string-join(for $word in $words return concat(upper-case(substring($word, 1, 1)), substring($word, 2)), '')"/>
    </xsl:function>
    
    

    <xsl:template match="/">
        <xsl:for-each select="//skos:ConceptScheme/skos:hasTopConcept">
            <xsl:variable name="topConceptUri" select="@rdf:resource"/>
            <xsl:variable name="topConcept" select="//skos:Concept[@rdf:about=$topConceptUri]"/>
           <!-- <xsl:text># ******
            </xsl:text>-->
            <xsl:variable name="filename" select="concat('../thesmatic/', translate(translate($topConcept/skos:prefLabel, ' ', '_'), 'é', 'e'), '.py')"/>
            <xsl:result-document href="{$filename}">
                <xsl:text>from pydantic import BaseModel
from typing import Union, Literal
                
</xsl:text>
            <xsl:apply-templates select="$topConcept" mode="topConcept"/>
            </xsl:result-document>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="skos:Concept" mode="topConcept">
        <xsl:variable name="normalizedLabel" select="fn:normalize-unicode(skos:prefLabel, 'NFC')"/>
        
        <!--<xsl:value-of select="$normalizedLabel"/>-->
       <!-- <xsl:variable name="className" select="concat('$', translate($normalizedLabel,' ',''), '$')"/>-->
        <xsl:variable name="className" select="translate(translate(my:toCamelCase(concat(translate($normalizedLabel,
            'àáâãäåçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ',
            'aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUY'), '')), '''', ''), '-', '')"/>
        
        <xsl:variable name="uri" select="@rdf:about"/>
        
        <xsl:text>class </xsl:text>
        <xsl:value-of select="$className"/>
        <xsl:text>(BaseModel):
    terme_specifique: </xsl:text>
        
        <xsl:choose>
            <xsl:when test="skos:narrower">
                <xsl:text>Union[</xsl:text>
                <xsl:for-each select="skos:narrower">
                    <xsl:variable name="narrowerUri" select="@rdf:resource"/>
                    <xsl:variable name="narrowerConcept" select="//skos:Concept[@rdf:about=$narrowerUri]"/>
                    <xsl:text>'</xsl:text>
                    <xsl:value-of select="translate(translate(concat('''', translate(
                                                       translate(fn:normalize-unicode(my:toCamelCase($narrowerConcept/skos:prefLabel), 'NFC'),
                                                       'àáâãäåçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ',
                                                       'aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUY'), 
                                                        ' ', ' '), 
                                           '''', ''), '''', ''), '-', '')"/>
                    <xsl:text>'</xsl:text>
                    <xsl:if test="position() != last()">
                        <xsl:text>, </xsl:text>
                    </xsl:if>
                </xsl:for-each>
                <xsl:text>]</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>Literal['</xsl:text>
                <xsl:value-of select="skos:prefLabel"/>
                <xsl:text>']</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        
        <xsl:text>
    ark: str = "</xsl:text>
        <xsl:value-of select="$uri"/>
        <xsl:text>"
    descripteur: str = "</xsl:text>
        <xsl:value-of select="skos:prefLabel"/>
        <xsl:text>"
</xsl:text>
        
        <xsl:apply-templates select="//skos:Concept[skos:broader/@rdf:resource=$uri]" mode="childConcept"/>
    </xsl:template>
    
    <xsl:template match="skos:Concept" mode="childConcept">
        <xsl:variable name="normalizedLabel" select="fn:normalize-unicode(skos:prefLabel, 'NFC')"/>
        <xsl:variable name="className" select="translate(translate(my:toCamelCase(concat(translate($normalizedLabel,
            'àáâãäåçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ',
            'aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUY'), '')), '''', ''), '-', '')"/>
        
        <xsl:variable name="uri" select="@rdf:about"/>
        
        <xsl:text>class </xsl:text>
        <xsl:value-of select="$className"/>
        <xsl:text>(BaseModel):
    terme_specifique: </xsl:text>
        
        <xsl:choose>
            <xsl:when test="skos:narrower">
                <xsl:text>Union[</xsl:text>
                <xsl:for-each select="skos:narrower">
                    <xsl:variable name="narrowerUri" select="@rdf:resource"/>
                    <xsl:variable name="narrowerConcept" select="//skos:Concept[@rdf:about=$narrowerUri]"/>
                    <xsl:value-of select="concat('''', translate(translate(
                        translate(
                        translate(fn:normalize-unicode(my:toCamelCase($narrowerConcept/skos:prefLabel), 'NFC'),
                        'àáâãäåçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ',
                        'aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUY'
                                ), '''', ''), 
                        ' ', ' '), '-', ''), 
                        '''', '')"/>
                    <xsl:if test="position() != last()">
                        <xsl:text>, </xsl:text>
                    </xsl:if>
                </xsl:for-each>
                <xsl:text>]</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>Literal['</xsl:text>
                <xsl:value-of select="
                    translate(translate(translate(fn:normalize-unicode(my:toCamelCase(skos:prefLabel), 'NFC'),
                    'àáâãäåçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ',
                    'aaaaaceeeeiiiinooooouuuuyyAAAAACEEEEIIIINOOOOOUUUUY'
                    ), '''', ''), '-', '')
                    "/>
                <xsl:text>']</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        
        <xsl:text>
    ark: str = "</xsl:text>
        <xsl:value-of select="$uri"/>
        <xsl:text>"
    descripteur: str = "</xsl:text>
        <xsl:value-of select="skos:prefLabel"/>
        <xsl:text>"
</xsl:text>
        
        <xsl:apply-templates select="//skos:Concept[skos:broader/@rdf:resource=$uri]" mode="childConcept"/>
    </xsl:template>
    
</xsl:stylesheet>
<!--from pydantic import BaseModel
from typing import Union, Literal-->

<!--for name, obj in globals().items():
    if isinstance(obj, type) and issubclass(obj, BaseModel):
        obj.update_forward_refs()
-->
