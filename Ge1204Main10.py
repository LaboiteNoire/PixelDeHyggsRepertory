import F1204Tekusucha10
import F1204Tekisuto10
import F1204Saundoefekuto10
import F1204Generals10
F1204Generals10.Fpx1211importGeneral()
"""Pixel de Hyggs"""
"""Main File"""
def gePxLoadImages(a,s,r):
    i, metaD =F1204Tekusucha10.Fpx1400loadImages(a,s,r)
    return i, metaD
def gePxTekisuto(s,n,i,si):
    F1204Tekisuto10.Fpx2601Tekisuto(s,n,i,si)
def gePxTekisutoArial(s,i,si):
    F1204Tekisuto10.Fpx2601TekisutoArial(s,i,si)
def gePxSaundoefekuto(n,x,y):
    metaD = F1204Saundoefekuto10.Fpx2401Saundoefekuto(n,x,y)
    return metaD
def gePxSaundoefekutoInit():
    F1204Saundoefekuto10.Fpx2401SaundoefekutoInit()
def gePxImportGeneral():
    metaD = F1204Generals10.Fpx1211importGeneral()
    return metaD
def gePxVariablesStatics():
    pi = F1204Generals10.Fpx1701variablesStatics()
    Variables = ["pi",pi]
    return Variables
def gePxCreateWindow(t,h,l,ti):
    Window, metaD = F1204Generals10.Gpx1211createWindow(t,h,l,ti)
    return Windows, metaD
