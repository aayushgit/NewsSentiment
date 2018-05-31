import re
def classifier(news):
    var = []
    # Regular Expression for ADBL
    ADBL = re.compile(r'(Agriculture\sDevelopment\sBank)|(ADBL)')
    if ADBL.search(news):
        var.append('ADBL')
    

    # Regular Expression for API
    API = re.compile(r'(Api\sPower\sCompany)|(API)')
    if API.search(news):
        var.append('API')
    

    # Regular Expression for AMFI
    AMFI = re.compile(r'(Arambha\sMicrofinance\sBittiya\sSanstha)|(AMFI)')
    if AMFI.search(news):
        var.append('AMFI')
     

    # Regular Expression for AKPL
    AKPL = re.compile(r'(Arun\sKabeli\sPower)|(AKPL)')
    if AKPL.search(news):
        var.append('AKPL')

    # Regular Expression for AHPC
    AHPC = re.compile(r'(Arun\sValley\sHydropower\sDevelopment\sCo)|(AHPC)')
    if AHPC.search(news):
        var.append('AHPC')

    # Regular Expression for AVU
    AVU = re.compile(r'(Arun\sVanaspati\sUdhyog)|(AVU)')
    if AVU.search(news):
        var.append('AVU')

    # Regular Expression for ALICL
    ALICL = re.compile(r'(Asian\sLife\sInsurance\sCo)|(ALICL)')
    if ALICL.search(news):
        var.append('ALICL')

    # Regular Expression for BOKL
    BOKL = re.compile(r'(Bank\sof\sKathmandu)|(BOKL)')
    if BOKL.search(news):
        var.append('BOKL')

    # Regular Expression for BARUN
    BARUN = re.compile(r'(Barun\sHydropower\sCo)|(BARUN)')
    if BARUN.search(news):
        var.append('BARUN')

    # Regular Expression for BFC
    BFC = re.compile(r'(Best\sFinance\sCompany)|(BFC)')
    if BFC.search(news):
        var.append('BFC')

    # Regular Expression for BHBL
    BHBL = re.compile(r'(Bhargav\sBikash\sBank)|(BHBL)')
    if BHBL.search(news):
        var.append('BHBL')

    # Regular Expression for BSL
    BSL = re.compile(r'(Birat\sShoe)|(BSL)')
    if BSL.search(news):
        var.append('BSL')

    # Regular Expression for BBC
    BBC = re.compile(r'(Bishal\sBazar\sCompany)|(BBC)')
    if BBC.search(news):
        var.append('BBC')

    # Regular Expression for BNL
    BNL = re.compile(r'(Bottlers\sNepal\sBalaju)|(BNL)')
    if BNL.search(news):
        var.append('BNL')

    # Regular Expression for BNT
    BNT = re.compile(r'(Bottlers\sNepal\sTerai)|(BNT)')
    if BNT.search(news):
        var.append('BNT')

    # Regular Expression for BPCL
    BPCL = re.compile(r'(Butwal\sPower\sCompany)|(BPCL)')
    if BPCL.search(news):
        var.append('BPCL')

    # Regular Expression for BSM
    BSM = re.compile(r'(Butwal\sSpinning\sMills)|(BSM)')
    if BSM.search(news):
        var.append('BSM')

    # Regular Expression for CMB
    CMB = re.compile(r'(Capital\sMerchant\sBank\sFinance\sCo)|(CMB)')
    if CMB.search(news):
        var.append('CMB')

    # Regular Expression for CFCL
    CFCL = re.compile(r'(Central\sFinance\sCo)|(CFCL)')
    if CFCL.search(news):
        var.append('CFCL')

    # Regular Expression for CCBL
    CCBL = re.compile(r'(Century\sCommercial\sBank)|(CCBL)')
    if CCBL.search(news):
        var.append('CCBL')

    # Regular Expression for CBBL
    CBBL = re.compile(r'(Chhimek\sLaghubitta\sBikas\sBank)|(CBBL)')
    if CBBL.search(news):
        var.append('CBBL')

    # Regular Expression for CHL
    CHL = re.compile(r'(Chhyangdi\sHydropower)|(CHL)')
    if CHL.search(news):
        var.append('CHL')

    # Regular Expression for CHCL
    CHCL = re.compile(r'(Chilime\sHydropower\sCompany)|(CHCL)')
    if CHCL.search(news):
        var.append('CHCL')

    # Regular Expression for CZBIL
    CZBIL = re.compile(r'(Citizen\sBank\sInternational)|(CZBIL)')
    if CZBIL.search(news):
        var.append('CZBIL')

    # Regular Expression for CIT
    CIT = re.compile(r'(Citizen\sInvestment\sTrust)|(CIT)')
    if CIT.search(news):
        var.append('CIT')

    # Regular Expression for CMF1
    CMF1 = re.compile(r'(Citizens\sMutual\sFund\s1)|(CMF1)')
    if CMF1.search(news):
        var.append('CMF1')

    # Regular Expression for CEFL
    CEFL = re.compile(r'(City\sExpress\sFinance\sCo)|(CEFL)')
    if CEFL.search(news):
        var.append('CEFL')

    # Regular Expression for CBL
    CBL = re.compile(r'(Civil\sBank)|(CBL)')
    if CBL.search(news):
        var.append('CBL')

    # Regular Expression for CLBSL
    CLBSL = re.compile(r'(Civil\sLaghubitta\sBittiya\sSanstha)|(CLBSL)')
    if CLBSL.search(news):
        var.append('CLBSL')

    # Regular Expression for CORBL
    CORBL = re.compile(r'(Corporate\sDevelopment\sBank)|(CORBL)')
    if CORBL.search(news):
        var.append('CORBL')

    # Regular Expression for CFL
    CFL = re.compile(r'(Crystal\sFinance)|(CFL)')
    if CFL.search(news):
        var.append('CFL')

    # Regular Expression for DDBL
    DDBL = re.compile(r'(Deprosc\sLaghubitta\sBittiya\sSanstha)|(DDBL)')
    if DDBL.search(news):
        var.append('DDBL')

    # Regular Expression for DBBL
    DBBL = re.compile(r'(Deva\sBikas\sBank)|(DBBL)')
    if DBBL.search(news):
        var.append('DBBL')

    # Regular Expression for DHPL
    DHPL = re.compile(r'(Dibyashwori\sHydropower)|(DHPL)')
    if DHPL.search(news):
        var.append('DHPL')

    # Regular Expression for EBL
    EBL = re.compile(r'(Everest\sBank)|(EBL)')
    if EBL.search(news):
        var.append('EBL')

    # Regular Expression for EBLCP
    EBLCP = re.compile(r'(Everest\sBank\sCon\sPref)|(EBLCP)')
    if EBLCP.search(news):
        var.append('EBLCP')

    # Regular Expression for EIC
    EIC = re.compile(r'(Everest\sInsurance\sCo)|(EIC)')
    if EIC.search(news):
        var.append('EIC')

    # Regular Expression for EDBL
    EDBL = re.compile(r'(Excel\sDevelopment\sBank)|(EDBL)')
    if EDBL.search(news):
        var.append('EDBL')

    # Regular Expression for FMDBL
    FMDBL = re.compile(r'(First\sMicro\sFinance\sDevelopment\sBank)|(FMDBL)')
    if FMDBL.search(news):
        var.append('FMDBL')

    # Regular Expression for FHL
    FHL = re.compile(r'(Fleur\sHimalayan)|(FHL)')
    if FHL.search(news):
        var.append('FHL')

    # Regular Expression for FOWAD
    FOWAD = re.compile(r'(Forward\sCommunity\sMicrofinance\sBittiya\sSanstha)|(FOWAD)')
    if FOWAD.search(news):
        var.append('FOWAD')

    # Regular Expression for GDBL
    GDBL = re.compile(r'(Gandaki\sBikas\sBank)|(GDBL)')
    if GDBL.search(news):
        var.append('GDBL')

    # Regular Expression for GBBL
    GBBL = re.compile(r'(Garima\sBikas\sBank)|(GBBL)')
    if GBBL.search(news):
        var.append('GBBL')

    # Regular Expression for GBIME
    GBIME = re.compile(r'(Global\sIME\sBank)|(GBIME)')
    if GBIME.search(news):
        var.append('GBIME')

    # Regular Expression for GILB
    GILB = re.compile(r'(Global\sIME\sLaghubitta\sBittiya\sSanstha)|(GILB)')
    if GILB.search(news):
        var.append('GILB')

    # Regular Expression for GIMES1
    GIMES1 = re.compile(r'(Global\sIME\sSamunnat\sScheme1)|(GIMES1)')
    if GIMES1.search(news):
        var.append('GIMES1')

    # Regular Expression for GFCL
    GFCL = re.compile(r'(Goodwill\sFinance\sCo)|(GFCL)')
    if GFCL.search(news):
        var.append('GFCL')

    # Regular Expression for GRU
    GRU = re.compile(r'(Gorakhkali\sRubber\sUdhyog)|(GRU)')
    if GRU.search(news):
        var.append('GRU')

    # Regular Expression for GBLBS
    GBLBS = re.compile(r'(Grameen\sBikas\sLaghubitta\sBittiya\sSanstha)|(GBLBS)')
    if GBLBS.search(news):
        var.append('GBLBS')

    # Regular Expression for GRDBL
    GRDBL = re.compile(r'(Green\sDevelopment\sBank)|(GRDBL)')
    if GRDBL.search(news):
        var.append('GRDBL')

    # Regular Expression for GMFIL
    GMFIL = re.compile(r'(Guheshowori\sMerchant\sBank\sFinance\sCo)|(GMFIL)')
    if GMFIL.search(news):
        var.append('GMFIL')

    # Regular Expression for GLICL
    GLICL = re.compile(r'(Gurans\sLife\sInsurance\sCompany)|(GLICL)')
    if GLICL.search(news):
        var.append('GLICL')

    # Regular Expression for GUFL
    GUFL = re.compile(r'(Gurkhas\sFinance)|(GUFL)')
    if GUFL.search(news):
        var.append('GUFL')

    # Regular Expression for HAMRO
    HAMRO = re.compile(r'(Hamro\sBikas\sBank)|(HAMRO)')
    if HAMRO.search(news):
        var.append('HAMRO')

    # Regular Expression for HBT
    HBT = re.compile(r'(Harisiddhi\sBrick\sAnd\sTiles)|(HBT)')
    if HBT.search(news):
        var.append('HBT')

    # Regular Expression for HATH
    HATH = re.compile(r'(Hathway\sFinance\sCompany)|(HATH)')
    if HATH.search(news):
        var.append('HATH')

    # Regular Expression for HBL
    HBL = re.compile(r'(Himalayan\sBank)|(HBL)')
    if HBL.search(news):
        var.append('HBL')

    # Regular Expression for HDL
    HDL = re.compile(r'(Himalayan\sDistillery)|(HDL)')
    if HDL.search(news):
        var.append('HDL')

    # Regular Expression for HFL
    HFL = re.compile(r'(Himalayan\sFinance\sBittiya\sSanstha)|(HFL)')
    if HFL.search(news):
        var.append('HFL')

    # Regular Expression for HGI
    HGI = re.compile(r'(Himalayan\sGeneral\sInsurance\sCo)|(HGI)')
    if HGI.search(news):
        var.append('HGI')

    # Regular Expression for HPPL
    HPPL = re.compile(r'(Himalayan\sPower\sPartner)|(HPPL)')
    if HPPL.search(news):
        var.append('HPPL')

    # Regular Expression for ICFC
    ICFC = re.compile(r'(ICFC\sFinance)|(ICFC)')
    if ICFC.search(news):
        var.append('ICFC')

    # Regular Expression for IGI
    IGI = re.compile(r'(IME\sGeneral\sInsurance)|(IGI)')
    if IGI.search(news):
        var.append('IGI')

    # Regular Expression for HIDCL
    HIDCL = re.compile(r'(Jalabidyut\sLagani\statha\sBikas\sCo)|(HIDCL)')
    if HIDCL.search(news):
        var.append('HIDCL')

    # Regular Expression for JFL
    JFL = re.compile(r'(Janaki\sFinance)|(JFL)')
    if JFL.search(news):
        var.append('JFL')

    # Regular Expression for JBNL
    JBNL = re.compile(r'(Janata\sBank\sNepal)|(JBNL)')
    if JBNL.search(news):
        var.append('JBNL')

    # Regular Expression for JSLBB
    JSLBB = re.compile(r'(Janautthan\sSamudayic\sLaghubitta\sBikas\sBank)|(JSLBB)')
    if JSLBB.search(news):
        var.append('JSLBB')

    # Regular Expression for JEFL
    JEFL = re.compile(r'(Jebils\sFinance)|(JEFL)')
    if JEFL.search(news):
        var.append('JEFL')

    # Regular Expression for JBBL
    JBBL = re.compile(r'(Jyoti\sBikas\sBank)|(JBBL)')
    if JBBL.search(news):
        var.append('JBBL')

    # Regular Expression for JSM
    JSM = re.compile(r'(Jyoti\sSinning\sMills)|(JSM)')
    if JSM.search(news):
        var.append('JSM')

    # Regular Expression for KEBL
    KEBL = re.compile(r'(Kabeli\sBikas\sBank)|(KEBL)')
    if KEBL.search(news):
        var.append('KEBL')

    # Regular Expression for KBBL
    KBBL = re.compile(r'(Kailash\sBikas\sBank)|(KBBL)')
    if KBBL.search(news):
        var.append('KBBL')

    # Regular Expression for KMCDB
    KMCDB = re.compile(r'(Kalika\sMicrocredit\sDevelopment\sBank)|(KMCDB)')
    if KMCDB.search(news):
        var.append('KMCDB')

    # Regular Expression for KSBBL
    KSBBL = re.compile(r'(Kamana\sSewa\sBikas\sBank)|(KSBBL)')
    if KSBBL.search(news):
        var.append('KSBBL')

    # Regular Expression for KADBL
    KADBL = re.compile(r'(Kanchan\sDevelopment\sBank)|(KADBL)')
    if KADBL.search(news):
        var.append('KADBL')

    # Regular Expression for KNBL
    KNBL = re.compile(r'(Kankai\sBikas\sBank)|(KNBL)')
    if KNBL.search(news):
        var.append('KNBL')

    # Regular Expression for KRBL
    KRBL = re.compile(r'(Karnali\sDevelopment\sBank)|(KRBL)')
    if KRBL.search(news):
        var.append('KRBL')

    # Regular Expression for KKHC
    KKHC = re.compile(r'(Khanikhola\sHydropower\sCo)|(KKHC)')
    if KKHC.search(news):
        var.append('KKHC')

    # Regular Expression for KMFL
    KMFL = re.compile(r'(Kisan\sMicrofinance\sBittiya\sSanstha)|(KMFL)')
    if KMFL.search(news):
        var.append('KMFL')

    # Regular Expression for KBL
    KBL = re.compile(r'(Kumari\sBank)|(KBL)')
    if KBL.search(news):
        var.append('KBL')

    # Regular Expression for LFC
    LFC = re.compile(r'(Lalitpur\sFinance)|(LFC)')
    if LFC.search(news):
        var.append('LFC')

    # Regular Expression for LBL
    LBL = re.compile(r'(Laxmi\sBank)|(LBL)')
    if LBL.search(news):
        var.append('LBL')

    # Regular Expression for LEMF
    LEMF = re.compile(r'(Laxmi\sEquity\sFund)|(LEMF)')
    if LEMF.search(news):
        var.append('LEMF')

    # Regular Expression for LLBS
    LLBS = re.compile(r'(Laxmi\sLaghubitta\sBittiya\sSanstha)|(LLBS)')
    if LLBS.search(news):
        var.append('LLBS')

    # Regular Expression for LVF1
    LVF1 = re.compile(r'(Laxmi\sValue\sFund1)|(LVF1)')
    if LVF1.search(news):
        var.append('LVF1')

    # Regular Expression for LICN
    LICN = re.compile(r'(Life\sInsurance\sCo\sNepal)|(LICN)')
    if LICN.search(news):
        var.append('LICN')

    # Regular Expression for LBBL
    LBBL = re.compile(r'(Lumbini\sBikas\sBank)|(LBBL)')
    if LBBL.search(news):
        var.append('LBBL')

    # Regular Expression for LGIL
    LGIL = re.compile(r'(Lumbini\sGeneral\sInsurance\sCo)|(LGIL)')
    if LGIL.search(news):
        var.append('LGIL')

    # Regular Expression for MBL
    MBL = re.compile(r'(Machhapuchhre\sBank)|(MBL)')
    if MBL.search(news):
        var.append('MBL')

    # Regular Expression for MLBL
    MLBL = re.compile(r'(Mahalaxmi\sBikas\sBank)|(MLBL)')
    if MLBL.search(news):
        var.append('MLBL')

    # Regular Expression for MSMBS
    MSMBS = re.compile(r'(Mahila\sSahayatra\sMicrofinance\sBittiya\sSanstha)|(MSMBS)')
    if MSMBS.search(news):
        var.append('MSMBS')

    # Regular Expression for MSLB
    MSLB = re.compile(r'(Mahuli\sSamudayik\sLaghubitta\sSanstha)|(MSLB)')
    if MSLB.search(news):
        var.append('MSLB')

    # Regular Expression for MFIL
    MFIL = re.compile(r'(Manjushree\sFinance)|(MFIL)')
    if MFIL.search(news):
        var.append('MFIL')

    # Regular Expression for MEGA
    MEGA = re.compile(r'(Mega\sBank\sNepal)|(MEGA)')
    if MEGA.search(news):
        var.append('MEGA')

    # Regular Expression for MERO
    MERO = re.compile(r'(Mero\sMicrofinance\sBittiya\sSanstha)|(MERO)')
    if MERO.search(news):
        var.append('MERO')

    # Regular Expression for MMFDB
    MMFDB = re.compile(r'(Mirmire\sMicrofinance\sDevelopment\sBank)|(MMFDB)')
    if MMFDB.search(news):
        var.append('MMFDB')

    # Regular Expression for MIDBL
    MIDBL = re.compile(r'(Mission\sDevelopment\sBank)|(MIDBL)')
    if MIDBL.search(news):
        var.append('MIDBL')

    # Regular Expression for MDB
    MDB = re.compile(r'(Miteri\sDevelopment\sBank)|(MDB)')
    if MDB.search(news):
        var.append('MDB')

    # Regular Expression for MLBBL
    MLBBL = re.compile(r'(Mithila\sLaghuBitta\sBikas\sBank)|(MLBBL)')
    if MLBBL.search(news):
        var.append('MLBBL')

    # Regular Expression for MMDBL
    MMDBL = re.compile(r'(Mount\sMakalu\sDevelopment\sBank)|(MMDBL)')
    if MMDBL.search(news):
        var.append('MMDBL')

    # Regular Expression for MNBBL
    MNBBL = re.compile(r'(Muktinath\sBikas\sBank)|(MNBBL)')
    if MNBBL.search(news):
        var.append('MNBBL')

    # Regular Expression for MPFL
    MPFL = re.compile(r'(Multipurpose\sFinance\sCompany)|(MPFL)')
    if MPFL.search(news):
        var.append('MPFL')

    # Regular Expression for NABIL
    NABIL = re.compile(r'(Nabil\sBank)|(NABIL)')
    if NABIL.search(news):
        var.append('NABIL')

    # Regular Expression for NEF
    NEF = re.compile(r'(Nabil\sEquity\sFund)|(NEF)')
    if NEF.search(news):
        var.append('NEF')

    # Regular Expression for NBBL
    NBBL = re.compile(r'(NagBeli\sLaghuBitta\sBikas\sBank)|(NBBL)')
    if NBBL.search(news):
        var.append('NBBL')

    # Regular Expression for NBSL
    NBSL = re.compile(r'(Namaste\sBittiya\sSanstha)|(NBSL)')
    if NBSL.search(news):
        var.append('NBSL')

    # Regular Expression for NABBC
    NABBC = re.compile(r'(Narayani\sDevelopment\sBank)|(NABBC)')
    if NABBC.search(news):
        var.append('NABBC')

    # Regular Expression for NHPC
    NHPC = re.compile(r'(National\sHydro\sPower\sCompany)|(NHPC)')
    if NHPC.search(news):
        var.append('NHPC')

    # Regular Expression for NLICL
    NLICL = re.compile(r'(National\sLife\sInsurance\sCo)|(NLICL)')
    if NLICL.search(news):
        var.append('NLICL')

    # Regular Expression for NMFBS
    NMFBS = re.compile(r'(National\sMicrofinance\sBittiya\sSanstha)|(NMFBS)')
    if NMFBS.search(news):
        var.append('NMFBS')

    # Regular Expression for NNLB
    NNLB = re.compile(r'(Naya\sNepal\sLaghubitta\sBikas\sBank)|(NNLB)')
    if NNLB.search(news):
        var.append('NNLB')

    # Regular Expression for NIL
    NIL = re.compile(r'(Neco\sInsurance\sCo)|(NIL)')
    if NIL.search(news):
        var.append('NIL')

    # Regular Expression for NBB
    NBB = re.compile(r'(Nepal\sBangladesh\sBank)|(NBB)')
    if NBB.search(news):
        var.append('NBB')

    # Regular Expression for NBL
    NBL = re.compile(r'(Nepal\sBank)|(NBL)')
    if NBL.search(news):
        var.append('NBL')

    # Regular Expression for NBBU
    NBBU = re.compile(r'(Nepal\sBitumin\sAnd\sBarrel\sUdhyog)|(NBBU)')
    if NBBU.search(news):
        var.append('NBBU')

    # Regular Expression for NCDB
    NCDB = re.compile(r'(Nepal\sCommunity\sDevelopment\sBank)|(NCDB)')
    if NCDB.search(news):
        var.append('NCDB')

    # Regular Expression for NCCB
    NCCB = re.compile(r'(Nepal\sCredit\sAnd\sCommercial\sBank)|(NCCB)')
    if NCCB.search(news):
        var.append('NCCB')

    # Regular Expression for NTC
    NTC = re.compile(r'(Nepal\sDoorsanchar\sComapany)|(NTC)')
    if NTC.search(news):
        var.append('NTC')

    # Regular Expression for NFD
    NFD = re.compile(r'(Nepal\sFilm\sDevelopment\sCompany)|(NFD)')
    if NFD.search(news):
        var.append('NFD')

    # Regular Expression for NFS
    NFS = re.compile(r'(Nepal\sFinance)|(NFS)')
    if NFS.search(news):
        var.append('NFS')

    # Regular Expression for NHDL
    NHDL = re.compile(r'(Nepal\sHydro\sDevelopers)|(NHDL)')
    if NHDL.search(news):
        var.append('NHDL')

    # Regular Expression for NICL
    NICL = re.compile(r'(Nepal\sInsurance\sCo)|(NICL)')
    if NICL.search(news):
        var.append('NICL')

    # Regular Expression for NIB
    NIB = re.compile(r'(Nepal\sInvestment\sBank)|(NIB)')
    if NIB.search(news):
        var.append('NIB')

    # Regular Expression for NKU
    NKU = re.compile(r'(Nepal\sKhadya\sUdhyog)|(NKU)')
    if NKU.search(news):
        var.append('NKU')

    # Regular Expression for NLIC
    NLIC = re.compile(r'(Nepal\sLife\sInsurance\sCo)|(NLIC)')
    if NLIC.search(news):
        var.append('NLIC')

    # Regular Expression for NLO
    NLO = re.compile(r'(Nepal\sLube\sOil)|(NLO)')
    if NLO.search(news):
        var.append('NLO')

    # Regular Expression for SBI
    SBI = re.compile(r'(Nepal\sSBI\sBank)|(SBI)')
    if SBI.search(news):
        var.append('SBI')

    # Regular Expression for NSM
    NSM = re.compile(r'(Nepal\sShare\sMarkets)|(NSM)')
    if NSM.search(news):
        var.append('NSM')

    # Regular Expression for NTL
    NTL = re.compile(r'(Nepal\sTading)|(NTL)')
    if NTL.search(news):
        var.append('NTL')

    # Regular Expression for NVG
    NVG = re.compile(r'(Nepal\sVanaspati\sGhee\sUdhyog)|(NVG)')
    if NVG.search(news):
        var.append('NVG')

    # Regular Expression for NWC
    NWC = re.compile(r'(Nepal\sWelfare\sCompany)|(NWC)')
    if NWC.search(news):
        var.append('NWC')

    # Regular Expression for NLBBL
    NLBBL = re.compile(r'(Nerude\sLaghubita\sBikas\sBank)|(NLBBL)')
    if NLBBL.search(news):
        var.append('NLBBL')

    # Regular Expression for NGPL
    NGPL = re.compile(r'(Ngadi\sGroup\sPower)|(NGPL)')
    if NGPL.search(news):
        var.append('NGPL')

    # Regular Expression for NIBLPF
    NIBLPF = re.compile(r'(NIBL\sPragati\sFund)|(NIBLPF)')
    if NIBLPF.search(news):
        var.append('NIBLPF')

    # Regular Expression for NIBSF1
    NIBSF1 = re.compile(r'(NIBL\sSamriddhi\sFund\s1)|(NIBSF1)')
    if NIBSF1.search(news):
        var.append('NIBSF1')

    # Regular Expression for NICA
    NICA = re.compile(r'(NIC\sAsia\sBank)|(NICA)')
    if NICA.search(news):
        var.append('NICA')

    # Regular Expression for NICGF
    NICGF = re.compile(r'(NIC\sAsia\sGrowth\sFund)|(NICGF)')
    if NICGF.search(news):
        var.append('NICGF')

    # Regular Expression for NIDC
    NIDC = re.compile(r'(NIDC\sDevelopment\sBank)|(NIDC)')
    if NIDC.search(news):
        var.append('NIDC')

    # Regular Expression for NUBL
    NUBL = re.compile(r'(Nirdhan\sUtthan\sBank)|(NUBL)')
    if NUBL.search(news):
        var.append('NUBL')

    # Regular Expression for NLG
    NLG = re.compile(r'(NLG\sInsurance\sCompany)|(NLG)')
    if NLG.search(news):
        var.append('NLG')

    # Regular Expression for NMBMF
    NMBMF = re.compile(r'(NMB\sMicrofinance\sBittiya\sSanstha)|(NMBMF)')
    if NMBMF.search(news):
        var.append('NMBMF')

    # Regular Expression for NMB
    NMB = re.compile(r'(NMB\sBank)|(NMB)')
    if NMB.search(news):
        var.append('NMB')

    # Regular Expression for NMBHF1
    NMBHF1 = re.compile(r'(NMB\sHybrid\sFund\sL1)|(NMBHF1)')
    if NMBHF1.search(news):
        var.append('NMBHF1')

    # Regular Expression for NMBSF1
    NMBSF1 = re.compile(r'(NMB\sSulav\sInvestment\sFund1)|(NMBSF1)')
    if NMBSF1.search(news):
        var.append('NMBSF1')

    # Regular Expression for ODBL
    ODBL = re.compile(r'(Om\sDevelopment\sBank)|(ODBL)')
    if ODBL.search(news):
        var.append('ODBL')

    # Regular Expression for OHL
    OHL = re.compile(r'(Oriental\sHotels)|(OHL)')
    if OHL.search(news):
        var.append('OHL')

    # Regular Expression for PFL
    PFL = re.compile(r'(Pokhara\sFinance)|(PFL)')
    if PFL.search(news):
        var.append('PFL')

    # Regular Expression for PRVU
    PRVU = re.compile(r'(Prabhu\sBank)|(PRVU)')
    if PRVU.search(news):
        var.append('PRVU')

    # Regular Expression for PRIN
    PRIN = re.compile(r'(Prabhu\sInsurance)|(PRIN)')
    if PRIN.search(news):
        var.append('PRIN')

    # Regular Expression for PIC
    PIC = re.compile(r'(Premier\sInsurance\sCo)|(PIC)')
    if PIC.search(news):
        var.append('PIC')

    # Regular Expression for PCBL
    PCBL = re.compile(r'(Prime\sCommercial\sBank)|(PCBL)')
    if PCBL.search(news):
        var.append('PCBL')

    # Regular Expression for PLIC
    PLIC = re.compile(r'(Prime\sLife\sInsurance\sCompany)|(PLIC)')
    if PLIC.search(news):
        var.append('PLIC')

    # Regular Expression for PROFL
    PROFL = re.compile(r'(ProgressiveFinance)|(PROFL)')
    if PROFL.search(news):
        var.append('PROFL')

    # Regular Expression for PICL
    PICL = re.compile(r'(Prudential\sInsurance\sCo)|(PICL)')
    if PICL.search(news):
        var.append('PICL')

    # Regular Expression for PURBL
    PURBL = re.compile(r'(Purnima\sBikas\sBank)|(PURBL)')
    if PURBL.search(news):
        var.append('PURBL')

    # Regular Expression for RADHI
    RADHI = re.compile(r'(Radhi\sBidyut\sCompany)|(RADHI)')
    if RADHI.search(news):
        var.append('RADHI')

    # Regular Expression for RJM
    RJM = re.compile(r'(Raghupati\sJute\sMills)|(RJM)')
    if RJM.search(news):
        var.append('RJM')

    # Regular Expression for RBCL
    RBCL = re.compile(r'(Rastriya\sBeema\sCompany)|(RBCL)')
    if RBCL.search(news):
        var.append('RBCL')

    # Regular Expression for RLFL
    RLFL = re.compile(r'(Reliance\sFinance)|(RLFL)')
    if RLFL.search(news):
        var.append('RLFL')

    # Regular Expression for RHPC
    RHPC = re.compile(r'(Ridi\sHydropower\sDevelopment\sCompany)|(RHPC)')
    if RHPC.search(news):
        var.append('RHPC')

    # Regular Expression for RSDC
    RSDC = re.compile(r'(RSDC\sLaghubitta\sBittiya\sSanstha)|(RSDC)')
    if RSDC.search(news):
        var.append('RSDC')

    # Regular Expression for RMDC
    RMDC = re.compile(r'(Rural\sMicrofinance\sDevelopment\sCentre)|(RMDC)')
    if RMDC.search(news):
        var.append('RMDC')

    # Regular Expression for SIC
    SIC = re.compile(r'(Sagarmatha\sInsurance\sCo)|(SIC)')
    if SIC.search(news):
        var.append('SIC')

    # Regular Expression for SHBL
    SHBL = re.compile(r'(Sahara\sBikas\sBank)|(SHBL)')
    if SHBL.search(news):
        var.append('SHBL')

    # Regular Expression for SBBLJ
    SBBLJ = re.compile(r'(Sahayogi\sBikas\sBank)|(SBBLJ)')
    if SBBLJ.search(news):
        var.append('SBBLJ')

    # Regular Expression for STC
    STC = re.compile(r'(Salt\sTrading\sCorporation)|(STC)')
    if STC.search(news):
        var.append('STC')

    # Regular Expression for SMATA
    SMATA = re.compile(r'(Samata\sMicrofinance\sBittiya\sSanstha)|(SMATA)')
    if SMATA.search(news):
        var.append('SMATA')

    # Regular Expression for SFC
    SFC = re.compile(r'(Samjhana\sFinance\sCo)|(SFC)')
    if SFC.search(news):
        var.append('SFC')

    # Regular Expression for SKBBL
    SKBBL = re.compile(r'(Sana\sKisan\sBikas\sBank)|(SKBBL)')
    if SKBBL.search(news):
        var.append('SKBBL')

    # Regular Expression for SANIMA
    SANIMA = re.compile(r'(Sanima\sBank)|(SANIMA)')
    if SANIMA.search(news):
        var.append('SANIMA')

    # Regular Expression for SAEF
    SAEF = re.compile(r'(Sanima\sEquity\sFund)|(SAEF)')
    if SAEF.search(news):
        var.append('SAEF')

    # Regular Expression for SHPC
    SHPC = re.compile(r'(Sanima\sMai\sHydropower)|(SHPC)')
    if SHPC.search(news):
        var.append('SHPC')

    # Regular Expression for SKDBL
    SKDBL = re.compile(r'(Saptakoshi\sDevelopment\sBank)|(SKDBL)')
    if SKDBL.search(news):
        var.append('SKDBL')

    # Regular Expression for SADBL
    SADBL = re.compile(r'(Shangrila\sDevelopment\sBank)|(SADBL)')
    if SADBL.search(news):
        var.append('SADBL')

    # Regular Expression for SICL
    SICL = re.compile(r'(Shikhar\sInsurance\sCo)|(SICL)')
    if SICL.search(news):
        var.append('SICL')

    # Regular Expression for SHINE
    SHINE = re.compile(r'(Shine\sResunga\sDevelopment\sBank)|(SHINE)')
    if SHINE.search(news):
        var.append('SHINE')

    # Regular Expression for SBPP
    SBPP = re.compile(r'(Shree\sBhrikuti\sPulp\sAnd\sPaper)|(SBPP)')
    if SBPP.search(news):
        var.append('SBPP')

    # Regular Expression for SIFC
    SIFC = re.compile(r'(Shree\sInvestment\sFinance\sCo)|(SIFC)')
    if SIFC.search(news):
        var.append('SIFC')

    # Regular Expression for SRS
    SRS = re.compile(r'(Shree\sRam\sSugar\sMills)|(SRS)')
    if SRS.search(news):
        var.append('SRS')

    # Regular Expression for SFFIL
    SFFIL = re.compile(r'(Shrijana\sFinance\sBittaya\sSanstha)|(SFFIL)')
    if SFFIL.search(news):
        var.append('SFFIL')

    # Regular Expression for SBL
    SBL = re.compile(r'(Siddhartha\sBank)|(SBL)')
    if SBL.search(news):
        var.append('SBL')

    # Regular Expression for SEF
    SEF = re.compile(r'(Siddhartha\sEquity\sFund)|(SEF)')
    if SEF.search(news):
        var.append('SEF')

    # Regular Expression for SEOS
    SEOS = re.compile(r'(Siddhartha\sEquity\sOrineted\sScheme)|(SEOS)')
    if SEOS.search(news):
        var.append('SEOS')

    # Regular Expression for SIL
    SIL = re.compile(r'(Siddhartha\sInsurance)|(SIL)')
    if SIL.search(news):
        var.append('SIL')

    # Regular Expression for SINDU
    SINDU = re.compile(r'(Sindhu\sBikash\sBank)|(SINDU)')
    if SINDU.search(news):
        var.append('SINDU')

    # Regular Expression for SHL
    SHL = re.compile(r'(Soaltee\sHotel)|(SHL)')
    if SHL.search(news):
        var.append('SHL')

    # Regular Expression for SCB
    SCB = re.compile(r'(Standard\sChartered\sBank)|(SCB)')
    if SCB.search(news):
        var.append('SCB')

    # Regular Expression for SMFDB
    SMFDB = re.compile(r'(Summit\sMicro\sFinance\sDevelopment\sBank)|(SMFDB)')
    if SMFDB.search(news):
        var.append('SMFDB')

    # Regular Expression for SRBL
    SRBL = re.compile(r'(Sunrise\sBank)|(SRBL)')
    if SRBL.search(news):
        var.append('SRBL')

    # Regular Expression for SMB
    SMB = re.compile(r'(Support\sMicrofinance\sBittiya\sSanstha)|(SMB)')
    if SMB.search(news):
        var.append('SMB')

    # Regular Expression for SLICL
    SLICL = re.compile(r'(Surya\sLife\sInsurance\sCompany)|(SLICL)')
    if SLICL.search(news):
        var.append('SLICL')

    # Regular Expression for SLBS
    SLBS = re.compile(r'(Suryodaya\sLaghubitta\sBittiya\sSanstha)|(SLBS)')
    if SLBS.search(news):
        var.append('SLBS')

    # Regular Expression for SWBBL
    SWBBL = re.compile(r'(Swabalamban\sLaghubitta\sBittiya\sSanstha)|(SWBBL)')
    if SWBBL.search(news):
        var.append('SWBBL')

    # Regular Expression for SDESI
    SDESI = re.compile(r'(Swadeshi\sLaghubitta\sBittiya\sSanstha)|(SDESI)')
    if SDESI.search(news):
        var.append('SDESI')

    # Regular Expression for SLBBL
    SLBBL = re.compile(r'(Swarojgar\sLaghu\sBitta\sBikas\sBank)|(SLBBL)')
    if SLBBL.search(news):
        var.append('SLBBL')

    # Regular Expression for SYFL
    SYFL = re.compile(r'(Synergy\sFinance)|(SYFL)')
    if SYFL.search(news):
        var.append('SYFL')

    # Regular Expression for SPDL
    SPDL = re.compile(r'(Synergy\sPower\sDevelopment)|(SPDL)')
    if SPDL.search(news):
        var.append('SPDL')

    # Regular Expression for TRH
    TRH = re.compile(r'(Taragaon\sRegency\sHotel)|(TRH)')
    if TRH.search(news):
        var.append('TRH')

    # Regular Expression for TNBL
    TNBL = re.compile(r'(Tinau\sDevelopment\sBank)|(TNBL)')
    if TNBL.search(news):
        var.append('TNBL')

    # Regular Expression for UNL
    UNL = re.compile(r'(Uniliver\sNepal)|(UNL)')
    if UNL.search(news):
        var.append('UNL')

    # Regular Expression for UFL
    UFL = re.compile(r'(United\sFinance)|(UFL)')
    if UFL.search(news):
        var.append('UFL')

    # Regular Expression for UIC
    UIC = re.compile(r'(United\sInsurance\sCo\sNepal)|(UIC)')
    if UIC.search(news):
        var.append('UIC')

    # Regular Expression for UMHL
    UMHL = re.compile(r'(United\sModi\sHydropower)|(UMHL)')
    if UMHL.search(news):
        var.append('UMHL')

    # Regular Expression for UMB
    UMB = re.compile(r'(Unnati\sMicorfinance\sBittiya\sSanstha)|(UMB)')
    if UMB.search(news):
        var.append('UMB')

    # Regular Expression for VLBS
    VLBS = re.compile(r'(Vijaya\slaghubitta\sBittiya\sSanstha)|(VLBS)')
    if VLBS.search(news):
        var.append('VLBS')

    # Regular Expression for WDBL
    WDBL = re.compile(r'(Western\sDevelopment\sBank)|(WDBL)')
    if WDBL.search(news):
        var.append('WDBL')

    # Regular Expression for WOMI
    WOMI = re.compile(r'(Womi\sMicrofinance\sBittiya\sSanstha)|(WOMI)')
    if WOMI.search(news):
        var.append('WOMI')

    # Regular Expression for WMBF
    WMBF = re.compile(r'(World\sMerchant\sBanking\sFinance)|(WMBF)')
    if WMBF.search(news):
        var.append('WMBF')

    # Regular Expression for YHL
    YHL = re.compile(r'(Yak\sAnd\sYeti\sHotel)|(YHL)')
    if YHL.search(news):
        var.append('YHL')

    return (var)