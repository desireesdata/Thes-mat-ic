<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:skos="http://www.w3.org/2004/02/skos/core#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    exclude-result-prefixes="#all"
    expand-text="yes">
    
    <xsl:output method="text" indent="no"/>
    
    <xsl:template match="/">
        <xsl:for-each select="//skos:ConceptScheme/skos:hasTopConcept">
            <xsl:variable name="topConceptUri" select="@rdf:resource"/>
            <xsl:variable name="topConcept" select="//skos:Concept[@rdf:about=$topConceptUri]"/>
            <xsl:variable name="filename" select="replace(concat(translate($topConcept/skos:prefLabel, ' ', '_'), '.txt'), 'é', 'e')"/>
            <xsl:variable name="content">
                <xsl:value-of select="$topConcept/skos:prefLabel"/>
                <xsl:text>(</xsl:text>
                <xsl:apply-templates select="//skos:Concept[skos:broader/@rdf:resource=$topConceptUri]" mode="childConcept">
                    <xsl:with-param name="position" select="position()"/>
                    <xsl:with-param name="last" select="last()"/>
                </xsl:apply-templates>
                <xsl:text>)</xsl:text>
            </xsl:variable>
            <xsl:variable name="transformedContent" select="replace($content, ';\s\)', ')')"/>
            
            <xsl:result-document href="../thesmatxt_min_flat/{$filename}">
                <xsl:value-of select="$transformedContent"/>
            </xsl:result-document>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="skos:Concept" mode="childConcept">
        <xsl:param name="indent"/>
        <xsl:variable name="prefLabel" select="skos:prefLabel"/>
        <xsl:value-of select="$indent"/>
        <xsl:text></xsl:text>
        <xsl:value-of select="$prefLabel"/>
        <xsl:text>; </xsl:text>
    </xsl:template>
    
</xsl:stylesheet>
