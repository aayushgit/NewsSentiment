import re

# n = 'Agriculture Development Bank Limited'
def classifier(news):

    # Regular Expression for ADBL
    ADBL = re.compile(r'(Agriculture\sDevelopment\sBank\sLimited)|(ADBL)')
    if ADBL.search(news):
        return ('ADBL')


    # Regular Expression for API
    API = re.compile(r'(Api\sPower\sCompany\sLtd)|(API)')
    if API.search(news):
        return ('API')

    # Regular Expression for AMFI
    AMFI = re.compile(r'(Arambha\sMicrofinance\sBittiya\sSanstha\sLtd)|(AMFI)')
    if AMFI.search(news):
        return ('AMFI')

    # Regular Expression for AKPL
    AKPL = re.compile(r'(Arun\sKabeli\sPower\sLtd)|(AKPL)')
    if AKPL.search(news):
        return ('AKPL')

    # Regular Expression for AHPC
    AHPC = re.compile(r'(Arun\sValley\sHydropower\sDevelopment\sCo\sLtd)|(AHPC)')
    if AHPC.search(news):
        return ('AHPC')

    # Regular Expression for AVU
    AVU = re.compile(r'(Arun\sVanaspati\sUdhyog\sLimited)|(AVU)')
    if AVU.search(news):
        return ('AVU')

    # Regular Expression for ALICL
    ALICL = re.compile(r'(Asian\sLife\sInsurance\sCo\sLimited)|(ALICL)')
    if ALICL.search(news):
        return ('ALICL')

    # Regular Expression for BOKL
    BOKL = re.compile(r'(Bank\sof\sKathmandu\sLtd)|(BOKL)')
    if BOKL.search(news):
        return ('BOKL')

    # Regular Expression for BARUN
    BARUN = re.compile(r'(Barun\sHydropower\sCo\sLtd)|(BARUN)')
    if BARUN.search(news):
        return ('BARUN')

    # Regular Expression for BFC
    BFC = re.compile(r'(Best\sFinance\sCompany\sLtd)|(BFC)')
    if BFC.search(news):
        return ('BFC')

    # Regular Expression for BHBL
    BHBL = re.compile(r'(Bhargav\sBikash\sBank\sLtd)|(BHBL)')
    if BHBL.search(news):
        return ('BHBL')

    # Regular Expression for BSL
    BSL = re.compile(r'(Birat\sShoe\sLimited)|(BSL)')
    if BSL.search(news):
        return ('BSL')

    # Regular Expression for BBC
    BBC = re.compile(r'(Bishal\sBazar\sCompany\sLimited)|(BBC)')
    if BBC.search(news):
        return ('BBC')

    # Regular Expression for BNL
    BNL = re.compile(r'(Bottlers\sNepal\sBalaju\sLimited)|(BNL)')
    if BNL.search(news):
        return ('BNL')

    # Regular Expression for BNT
    BNT = re.compile(r'(Bottlers\sNepal\sTerai\sLimited)|(BNT)')
    if BNT.search(news):
        return ('BNT')

    # Regular Expression for BPCL
    BPCL = re.compile(r'(Butwal\sPower\sCompany\sLimited)|(BPCL)')
    if BPCL.search(news):
        return ('BPCL')

    # Regular Expression for BSM
    BSM = re.compile(r'(Butwal\sSpinning\sMills\sLimited)|(BSM)')
    if BSM.search(news):
        return ('BSM')

    # Regular Expression for CMB
    CMB = re.compile(r'(Capital\sMerchant\sBank\sFinance\sCo\sLtd)|(CMB)')
    if CMB.search(news):
        return ('CMB')

    # Regular Expression for CFCL
    CFCL = re.compile(r'(Central\sFinance\sCo\sLtd)|(CFCL)')
    if CFCL.search(news):
        return ('CFCL')

    # Regular Expression for CCBL
    CCBL = re.compile(r'(Century\sCommercial\sBank\sLtd)|(CCBL)')
    if CCBL.search(news):
        return ('CCBL')

    # Regular Expression for CBBL
    CBBL = re.compile(r'(Chhimek\sLaghubitta\sBikas\sBank\sLimited)|(CBBL)')
    if CBBL.search(news):
        return ('CBBL')

    # Regular Expression for CHL
    CHL = re.compile(r'(Chhyangdi\sHydropower\sLtd)|(CHL)')
    if CHL.search(news):
        return ('CHL')

    # Regular Expression for CHCL
    CHCL = re.compile(r'(Chilime\sHydropower\sCompany\sLimited)|(CHCL)')
    if CHCL.search(news):
        return ('CHCL')

    # Regular Expression for CZBIL
    CZBIL = re.compile(r'(Citizen\sBank\sInternational\sLimited)|(CZBIL)')
    if CZBIL.search(news):
        return ('CZBIL')

    # Regular Expression for CIT
    CIT = re.compile(r'(Citizen\sInvestment\sTrust)|(CIT)')
    if CIT.search(news):
        return ('CIT')

    # Regular Expression for CMF1
    CMF1 = re.compile(r'(Citizens\sMutual\sFund\s1)|(CMF1)')
    if CMF1.search(news):
        return ('CMF1')

    # Regular Expression for CEFL
    CEFL = re.compile(r'(City\sExpress\sFinance\sCo\sLimited)|(CEFL)')
    if CEFL.search(news):
        return ('CEFL')

    # Regular Expression for CBL
    CBL = re.compile(r'(Civil\sBank\sLtd)|(CBL)')
    if CBL.search(news):
        return ('CBL')

    # Regular Expression for CLBSL
    CLBSL = re.compile(r'(Civil\sLaghubitta\sBittiya\sSanstha\sLtd)|(CLBSL)')
    if CLBSL.search(news):
        return ('CLBSL')

    # Regular Expression for CORBL
    CORBL = re.compile(r'(Corporate\sDevelopment\sBank\sLimited)|(CORBL)')
    if CORBL.search(news):
        return ('CORBL')

    # Regular Expression for CFL
    CFL = re.compile(r'(Crystal\sFinance\sLtd)|(CFL)')
    if CFL.search(news):
        return ('CFL')

    # Regular Expression for DDBL
    DDBL = re.compile(r'(Deprosc\sDevelopment\sBank\sLimited)|(DDBL)')
    if DDBL.search(news):
        return ('DDBL')

    # Regular Expression for DBBL
    DBBL = re.compile(r'(Deva\sBikas\sBank\sLimited)|(DBBL)')
    if DBBL.search(news):
        return ('DBBL')

    # Regular Expression for DHPL
    DHPL = re.compile(r'(Dibyashwori\sHydropower\sLtd)|(DHPL)')
    if DHPL.search(news):
        return ('DHPL')

    # Regular Expression for EBL
    EBL = re.compile(r'(Everest\sBank\sLimited)|(EBL)')
    if EBL.search(news):
        return ('EBL')

    # Regular Expression for EBLCP
    EBLCP = re.compile(r'(Everest\sBank\sLimited\sCon\sPref)|(EBLCP)')
    if EBLCP.search(news):
        return ('EBLCP')

    # Regular Expression for EIC
    EIC = re.compile(r'(Everest\sInsurance\sCo\sLtd)|(EIC)')
    if EIC.search(news):
        return ('EIC')

    # Regular Expression for EDBL
    EDBL = re.compile(r'(Excel\sDevelopment\sBank\sLtd)|(EDBL)')
    if EDBL.search(news):
        return ('EDBL')

    # Regular Expression for FMDBL
    FMDBL = re.compile(r'(First\sMicro\sFinance\sDevelopment\sBank\sLtd)|(FMDBL)')
    if FMDBL.search(news):
        return ('FMDBL')

    # Regular Expression for FHL
    FHL = re.compile(r'(Fleur\sHimalayan\sLimited)|(FHL)')
    if FHL.search(news):
        return ('FHL')

    # Regular Expression for FOWAD
    FOWAD = re.compile(r'(Forward\sCommunity\sMicrofinance\sBittiya\sSanstha\sLtd)|(FOWAD)')
    if FOWAD.search(news):
        return ('FOWAD')

    # Regular Expression for GDBL
    GDBL = re.compile(r'(Gandaki\sBikas\sBank\sLimited)|(GDBL)')
    if GDBL.search(news):
        return ('GDBL')

    # Regular Expression for GBBL
    GBBL = re.compile(r'(Garima\sBikas\sBank\sLimited)|(GBBL)')
    if GBBL.search(news):
        return ('GBBL')

    # Regular Expression for GBIME
    GBIME = re.compile(r'(Global\sIME\sBank\sLimited)|(GBIME)')
    if GBIME.search(news):
        return ('GBIME')

    # Regular Expression for GILB
    GILB = re.compile(r'(Global\sIME\sLaghubitta\sBittiya\sSanstha\sLtd)|(GILB)')
    if GILB.search(news):
        return ('GILB')

    # Regular Expression for GIMES1
    GIMES1 = re.compile(r'(Global\sIME\sSamunnat\sScheme1)|(GIMES1)')
    if GIMES1.search(news):
        return ('GIMES1')

    # Regular Expression for GFCL
    GFCL = re.compile(r'(Goodwill\sFinance\sCo\sLtd)|(GFCL)')
    if GFCL.search(news):
        return ('GFCL')

    # Regular Expression for GRU
    GRU = re.compile(r'(Gorakhkali\sRubber\sUdhyog\sLimited)|(GRU)')
    if GRU.search(news):
        return ('GRU')

    # Regular Expression for GBLBS
    GBLBS = re.compile(r'(Grameen\sBikas\sLaghubitta\sBittiya\sSanstha\sLtd)|(GBLBS)')
    if GBLBS.search(news):
        return ('GBLBS')

    # Regular Expression for GRDBL
    GRDBL = re.compile(r'(Green\sDevelopment\sBank\sLtd)|(GRDBL)')
    if GRDBL.search(news):
        return ('GRDBL')

    # Regular Expression for GMFIL
    GMFIL = re.compile(r'(Guheshowori\sMerchant\sBank\sFinance\sCo\sLtd)|(GMFIL)')
    if GMFIL.search(news):
        return ('GMFIL')

    # Regular Expression for GLICL
    GLICL = re.compile(r'(Gurans\sLife\sInsurance\sCompany\sLtd)|(GLICL)')
    if GLICL.search(news):
        return ('GLICL')

    # Regular Expression for GUFL
    GUFL = re.compile(r'(Gurkhas\sFinance\sLtd)|(GUFL)')
    if GUFL.search(news):
        return ('GUFL')

    # Regular Expression for HAMRO
    HAMRO = re.compile(r'(Hamro\sBikas\sBank\sLtd)|(HAMRO)')
    if HAMRO.search(news):
        return ('HAMRO')

    # Regular Expression for HBT
    HBT = re.compile(r'(Harisiddhi\sBrick\sAnd\sTiles\sLimited)|(HBT)')
    if HBT.search(news):
        return ('HBT')

    # Regular Expression for HATH
    HATH = re.compile(r'(Hathway\sFinance\sCompany\sLimited)|(HATH)')
    if HATH.search(news):
        return ('HATH')

    # Regular Expression for HBL
    HBL = re.compile(r'(Himalayan\sBank\sLimited)|(HBL)')
    if HBL.search(news):
        return ('HBL')

    # Regular Expression for HDL
    HDL = re.compile(r'(Himalayan\sDistillery\sLimited)|(HDL)')
    if HDL.search(news):
        return ('HDL')

    # Regular Expression for HFL
    HFL = re.compile(r'(Himalayan\sFinance\sLimited\sBittiya\sSanstha)|(HFL)')
    if HFL.search(news):
        return ('HFL')

    # Regular Expression for HGI
    HGI = re.compile(r'(Himalayan\sGeneral\sInsurance\sCo\sLtd)|(HGI)')
    if HGI.search(news):
        return ('HGI')

    # Regular Expression for HPPL
    HPPL = re.compile(r'(Himalayan\sPower\sPartner\sLtd)|(HPPL)')
    if HPPL.search(news):
        return ('HPPL')

    # Regular Expression for ICFC
    ICFC = re.compile(r'(ICFC\sFinance\sLimited)|(ICFC)')
    if ICFC.search(news):
        return ('ICFC')

    # Regular Expression for IGI
    IGI = re.compile(r'(IME\sGeneral\sInsurance\sLtd)|(IGI)')
    if IGI.search(news):
        return ('IGI')

    # Regular Expression for HIDCL
    HIDCL = re.compile(r'(Jalabidyut\sLagani\statha\sBikas\sCo\sLtd)|(HIDCL)')
    if HIDCL.search(news):
        return ('HIDCL')

    # Regular Expression for JFL
    JFL = re.compile(r'(Janaki\sFinance\sLtd)|(JFL)')
    if JFL.search(news):
        return ('JFL')

    # Regular Expression for JBNL
    JBNL = re.compile(r'(Janata\sBank\sNepal\sLtd)|(JBNL)')
    if JBNL.search(news):
        return ('JBNL')

    # Regular Expression for JSLBB
    JSLBB = re.compile(r'(Janautthan\sSamudayic\sLaghubitta\sBikas\sBank\sLtd)|(JSLBB)')
    if JSLBB.search(news):
        return ('JSLBB')

    # Regular Expression for JEFL
    JEFL = re.compile(r'(Jebils\sFinance\sLtd)|(JEFL)')
    if JEFL.search(news):
        return ('JEFL')

    # Regular Expression for JBBL
    JBBL = re.compile(r'(Jyoti\sBikas\sBank\sLimited)|(JBBL)')
    if JBBL.search(news):
        return ('JBBL')

    # Regular Expression for JSM
    JSM = re.compile(r'(Jyoti\sSinning\sMills\sLimited)|(JSM)')
    if JSM.search(news):
        return ('JSM')

    # Regular Expression for KEBL
    KEBL = re.compile(r'(Kabeli\sBikas\sBank\sLimited)|(KEBL)')
    if KEBL.search(news):
        return ('KEBL')

    # Regular Expression for KBBL
    KBBL = re.compile(r'(Kailash\sBikas\sBank\sLtd)|(KBBL)')
    if KBBL.search(news):
        return ('KBBL')

    # Regular Expression for KMCDB
    KMCDB = re.compile(r'(Kalika\sMicrocredit\sDevelopment\sBank\sLtd)|(KMCDB)')
    if KMCDB.search(news):
        return ('KMCDB')

    # Regular Expression for KSBBL
    KSBBL = re.compile(r'(Kamana\sSewa\sBikas\sBank\sLimited)|(KSBBL)')
    if KSBBL.search(news):
        return ('KSBBL')

    # Regular Expression for KADBL
    KADBL = re.compile(r'(Kanchan\sDevelopment\sBank\sLimited)|(KADBL)')
    if KADBL.search(news):
        return ('KADBL')

    # Regular Expression for KNBL
    KNBL = re.compile(r'(Kankai\sBikas\sBank\sLtd)|(KNBL)')
    if KNBL.search(news):
        return ('KNBL')

    # Regular Expression for KRBL
    KRBL = re.compile(r'(Karnali\sDevelopment\sBank\sLimited)|(KRBL)')
    if KRBL.search(news):
        return ('KRBL')

    # Regular Expression for KKHC
    KKHC = re.compile(r'(Khanikhola\sHydropower\sCo\sLtd)|(KKHC)')
    if KKHC.search(news):
        return ('KKHC')

    # Regular Expression for KMFL
    KMFL = re.compile(r'(Kisan\sMicrofinance\sBittiya\sSanstha\sLtd)|(KMFL)')
    if KMFL.search(news):
        return ('KMFL')

    # Regular Expression for KBL
    KBL = re.compile(r'(Kumari\sBank\sLimited)|(KBL)')
    if KBL.search(news):
        return ('KBL')

    # Regular Expression for LFC
    LFC = re.compile(r'(Lalitpur\sFinance\sLtd)|(LFC)')
    if LFC.search(news):
        return ('LFC')

    # Regular Expression for LBL
    LBL = re.compile(r'(Laxmi\sBank\sLimited)|(LBL)')
    if LBL.search(news):
        return ('LBL')

    # Regular Expression for LEMF
    LEMF = re.compile(r'(Laxmi\sEquity\sFund)|(LEMF)')
    if LEMF.search(news):
        return ('LEMF')

    # Regular Expression for LLBS
    LLBS = re.compile(r'(Laxmi\sLaghubitta\sBittiya\sSanstha\sLtd)|(LLBS)')
    if LLBS.search(news):
        return ('LLBS')

    # Regular Expression for LVF1
    LVF1 = re.compile(r'(Laxmi\sValue\sFund1)|(LVF1)')
    if LVF1.search(news):
        return ('LVF1')

    # Regular Expression for LICN
    LICN = re.compile(r'(Life\sInsurance\sCo\sNepal)|(LICN)')
    if LICN.search(news):
        return ('LICN')

    # Regular Expression for LBBL
    LBBL = re.compile(r'(Lumbini\sBikas\sBank\sLtd)|(LBBL)')
    if LBBL.search(news):
        return ('LBBL')

    # Regular Expression for LGIL
    LGIL = re.compile(r'(Lumbini\sGeneral\sInsurance\sCo\sLtd)|(LGIL)')
    if LGIL.search(news):
        return ('LGIL')

    # Regular Expression for MBL
    MBL = re.compile(r'(Machhapuchhre\sBank\sLimited)|(MBL)')
    if MBL.search(news):
        return ('MBL')

    # Regular Expression for MLBL
    MLBL = re.compile(r'(Mahalaxmi\sBikas\sBank\sLtd)|(MLBL)')
    if MLBL.search(news):
        return ('MLBL')

    # Regular Expression for MSMBS
    MSMBS = re.compile(r'(Mahila\sSahayatra\sMicrofinance\sBittiya\sSanstha\sLtd)|(MSMBS)')
    if MSMBS.search(news):
        return ('MSMBS')

    # Regular Expression for MSLB
    MSLB = re.compile(r'(Mahuli\sSamudayik\sLaghubitta\sSanstha\sLtd)|(MSLB)')
    if MSLB.search(news):
        return ('MSLB')

    # Regular Expression for MFIL
    MFIL = re.compile(r'(Manjushree\sFinance\sLtd)|(MFIL)')
    if MFIL.search(news):
        return ('MFIL')

    # Regular Expression for MEGA
    MEGA = re.compile(r'(Mega\sBank\sNepal\sLtd)|(MEGA)')
    if MEGA.search(news):
        return ('MEGA')

    # Regular Expression for MERO
    MERO = re.compile(r'(Mero\sMicrofinance\sBittiya\sSanstha\sLtd)|(MERO)')
    if MERO.search(news):
        return ('MERO')

    # Regular Expression for MMFDB
    MMFDB = re.compile(r'(Mirmire\sMicrofinance\sDevelopment\sBank\sLtd)|(MMFDB)')
    if MMFDB.search(news):
        return ('MMFDB')

    # Regular Expression for MIDBL
    MIDBL = re.compile(r'(Mission\sDevelopment\sBank\sLtd)|(MIDBL)')
    if MIDBL.search(news):
        return ('MIDBL')

    # Regular Expression for MDB
    MDB = re.compile(r'(Miteri\sDevelopment\sBank\sLimited)|(MDB)')
    if MDB.search(news):
        return ('MDB')

    # Regular Expression for MLBBL
    MLBBL = re.compile(r'(Mithila\sLaghuBitta\sBikas\sBank\sLtd)|(MLBBL)')
    if MLBBL.search(news):
        return ('MLBBL')

    # Regular Expression for MMDBL
    MMDBL = re.compile(r'(Mount\sMakalu\sDevelopment\sBank\sLtd)|(MMDBL)')
    if MMDBL.search(news):
        return ('MMDBL')

    # Regular Expression for MNBBL
    MNBBL = re.compile(r'(Muktinath\sBikas\sBank\sLtd)|(MNBBL)')
    if MNBBL.search(news):
        return ('MNBBL')

    # Regular Expression for MPFL
    MPFL = re.compile(r'(Multipurpose\sFinance\sCompany\sLimited)|(MPFL)')
    if MPFL.search(news):
        return ('MPFL')

    # Regular Expression for NABIL
    NABIL = re.compile(r'(Nabil\sBank\sLimited)|(NABIL)')
    if NABIL.search(news):
        return ('NABIL')

    # Regular Expression for NEF
    NEF = re.compile(r'(Nabil\sEquity\sFund)|(NEF)')
    if NEF.search(news):
        return ('NEF')

    # Regular Expression for NBBL
    NBBL = re.compile(r'(NagBeli\sLaghuBitta\sBikas\sBank\sLtd)|(NBBL)')
    if NBBL.search(news):
        return ('NBBL')

    # Regular Expression for NBSL
    NBSL = re.compile(r'(Namaste\sBittiya\sSanstha\sLtd)|(NBSL)')
    if NBSL.search(news):
        return ('NBSL')

    # Regular Expression for NABBC
    NABBC = re.compile(r'(Narayani\sDevelopment\sBank\sLimited)|(NABBC)')
    if NABBC.search(news):
        return ('NABBC')

    # Regular Expression for NHPC
    NHPC = re.compile(r'(National\sHydro\sPower\sCompany\sLimited)|(NHPC)')
    if NHPC.search(news):
        return ('NHPC')

    # Regular Expression for NLICL
    NLICL = re.compile(r'(National\sLife\sInsurance\sCo\sLtd)|(NLICL)')
    if NLICL.search(news):
        return ('NLICL')

    # Regular Expression for NMFBS
    NMFBS = re.compile(r'(National\sMicrofinance\sBittiya\sSanstha\sLtd)|(NMFBS)')
    if NMFBS.search(news):
        return ('NMFBS')

    # Regular Expression for NNLB
    NNLB = re.compile(r'(Naya\sNepal\sLaghubitta\sBikas\sBank\sLtd)|(NNLB)')
    if NNLB.search(news):
        return ('NNLB')

    # Regular Expression for NIL
    NIL = re.compile(r'(Neco\sInsurance\sCo\sLtd)|(NIL)')
    if NIL.search(news):
        return ('NIL')

    # Regular Expression for NBB
    NBB = re.compile(r'(Nepal\sBangladesh\sBank\sLimited)|(NBB)')
    if NBB.search(news):
        return ('NBB')

    # Regular Expression for NBL
    NBL = re.compile(r'(Nepal\sBank\sLimited)|(NBL)')
    if NBL.search(news):
        return ('NBL')

    # Regular Expression for NBBU
    NBBU = re.compile(r'(Nepal\sBitumin\sAnd\sBarrel\sUdhyog\sLimited)|(NBBU)')
    if NBBU.search(news):
        return ('NBBU')

    # Regular Expression for NCCB
    NCCB = re.compile(r'(Nepal\sCredit\sAnd\sCommercial\sBank\sLimited)|(NCCB)')
    if NCCB.search(news):
        return ('NCCB')

    # Regular Expression for NTC
    NTC = re.compile(r'(Nepal\sDoorsanchar\sComapany\sLimited)|(NTC)')
    if NTC.search(news):
        return ('NTC')

    # Regular Expression for NFD
    NFD = re.compile(r'(Nepal\sFilm\sDevelopment\sCompany\sLimited)|(NFD)')
    if NFD.search(news):
        return ('NFD')

    # Regular Expression for NFS
    NFS = re.compile(r'(Nepal\sFinance\sLtd)|(NFS)')
    if NFS.search(news):
        return ('NFS')

    # Regular Expression for NHDL
    NHDL = re.compile(r'(Nepal\sHydro\sDevelopers\sLtd)|(NHDL)')
    if NHDL.search(news):
        return ('NHDL')

    # Regular Expression for NICL
    NICL = re.compile(r'(Nepal\sInsurance\sCo\sLtd)|(NICL)')
    if NICL.search(news):
        return ('NICL')

    # Regular Expression for NIB
    NIB = re.compile(r'(Nepal\sInvestment\sBank\sLimited)|(NIB)')
    if NIB.search(news):
        return ('NIB')

    # Regular Expression for NKU
    NKU = re.compile(r'(Nepal\sKhadya\sUdhyog\sLimited)|(NKU)')
    if NKU.search(news):
        return ('NKU')

    # Regular Expression for NLIC
    NLIC = re.compile(r'(Nepal\sLife\sInsurance\sCo\sLtd)|(NLIC)')
    if NLIC.search(news):
        return ('NLIC')

    # Regular Expression for NLO
    NLO = re.compile(r'(Nepal\sLube\sOil\sLimited)|(NLO)')
    if NLO.search(news):
        return ('NLO')

    # Regular Expression for SBI
    SBI = re.compile(r'(Nepal\sSBI\sBank\sLimited)|(SBI)')
    if SBI.search(news):
        return ('SBI')

    # Regular Expression for NSM
    NSM = re.compile(r'(Nepal\sShare\sMarkets\sLtd)|(NSM)')
    if NSM.search(news):
        return ('NSM')

    # Regular Expression for NTL
    NTL = re.compile(r'(Nepal\sTading\sLimited)|(NTL)')
    if NTL.search(news):
        return ('NTL')

    # Regular Expression for NVG
    NVG = re.compile(r'(Nepal\sVanaspati\sGhee\sUdhyog\sLimited)|(NVG)')
    if NVG.search(news):
        return ('NVG')

    # Regular Expression for NWC
    NWC = re.compile(r'(Nepal\sWelfare\sCompany\sLimited)|(NWC)')
    if NWC.search(news):
        return ('NWC')

    # Regular Expression for NLBBL
    NLBBL = re.compile(r'(Nerude\sLaghubita\sBikas\sBank\sLimited)|(NLBBL)')
    if NLBBL.search(news):
        return ('NLBBL')

    # Regular Expression for NGPL
    NGPL = re.compile(r'(Ngadi\sGroup\sPower\sLtd)|(NGPL)')
    if NGPL.search(news):
        return ('NGPL')

    # Regular Expression for NIBLPF
    NIBLPF = re.compile(r'(NIBL\sPragati\sFund)|(NIBLPF)')
    if NIBLPF.search(news):
        return ('NIBLPF')

    # Regular Expression for NIBSF1
    NIBSF1 = re.compile(r'(NIBL\sSamriddhi\sFund\s1)|(NIBSF1)')
    if NIBSF1.search(news):
        return ('NIBSF1')

    # Regular Expression for NICA
    NICA = re.compile(r'(NIC\sAsia\sBank\sLtd)|(NICA)')
    if NICA.search(news):
        return ('NICA')

    # Regular Expression for NICGF
    NICGF = re.compile(r'(NIC\sAsia\sGrowth\sFund)|(NICGF)')
    if NICGF.search(news):
        return ('NICGF')

    # Regular Expression for NIDC
    NIDC = re.compile(r'(NIDC\sDevelopment\sBank\sLtd)|(NIDC)')
    if NIDC.search(news):
        return ('NIDC')

    # Regular Expression for NUBL
    NUBL = re.compile(r'(Nirdhan\sUtthan\sBank\sLimited)|(NUBL)')
    if NUBL.search(news):
        return ('NUBL')

    # Regular Expression for NLG
    NLG = re.compile(r'(NLG\sInsurance\sCompany\sLtd)|(NLG)')
    if NLG.search(news):
        return ('NLG')

    # Regular Expression for NMBMF
    NMBMF = re.compile(r'(NMB\sMicrofinance\sBittiya\sSanstha\sLtd)|(NMBMF)')
    if NMBMF.search(news):
        return ('NMBMF')

    # Regular Expression for NMB
    NMB = re.compile(r'(NMB\sBank\sLimited)|(NMB)')
    if NMB.search(news):
        return ('NMB')

    # Regular Expression for NMBHF1
    NMBHF1 = re.compile(r'(NMB\sHybrid\sFund\sL1)|(NMBHF1)')
    if NMBHF1.search(news):
        return ('NMBHF1')

    # Regular Expression for NMBSF1
    NMBSF1 = re.compile(r'(NMB\sSulav\sInvestment\sFund1)|(NMBSF1)')
    if NMBSF1.search(news):
        return ('NMBSF1')

    # Regular Expression for ODBL
    ODBL = re.compile(r'(Om\sDevelopment\sBank\sLtd)|(ODBL)')
    if ODBL.search(news):
        return ('ODBL')

    # Regular Expression for OHL
    OHL = re.compile(r'(Oriental\sHotels\sLimited)|(OHL)')
    if OHL.search(news):
        return ('OHL')

    # Regular Expression for PFL
    PFL = re.compile(r'(Pokhara\sFinance\sLtd)|(PFL)')
    if PFL.search(news):
        return ('PFL')

    # Regular Expression for PRVU
    PRVU = re.compile(r'(Prabhu\sBank\sLimited)|(PRVU)')
    if PRVU.search(news):
        return ('PRVU')

    # Regular Expression for PRIN
    PRIN = re.compile(r'(Prabhu\sInsurance\sLtd)|(PRIN)')
    if PRIN.search(news):
        return ('PRIN')

    # Regular Expression for PIC
    PIC = re.compile(r'(Premier\sInsurance\sCo\sLtd)|(PIC)')
    if PIC.search(news):
        return ('PIC')

    # Regular Expression for PCBL
    PCBL = re.compile(r'(Prime\sCommercial\sBank\sLtd)|(PCBL)')
    if PCBL.search(news):
        return ('PCBL')

    # Regular Expression for PLIC
    PLIC = re.compile(r'(Prime\sLife\sInsurance\sCompany\sLimited)|(PLIC)')
    if PLIC.search(news):
        return ('PLIC')

    # Regular Expression for PROFL
    PROFL = re.compile(r'(ProgressiveFinance\sLimited)|(PROFL)')
    if PROFL.search(news):
        return ('PROFL')

    # Regular Expression for PICL
    PICL = re.compile(r'(Prudential\sInsurance\sCo\sLtd)|(PICL)')
    if PICL.search(news):
        return ('PICL')

    # Regular Expression for PURBL
    PURBL = re.compile(r'(Purnima\sBikas\sBank\sLtd)|(PURBL)')
    if PURBL.search(news):
        return ('PURBL')

    # Regular Expression for RADHI
    RADHI = re.compile(r'(Radhi\sBidyut\sCompany\sLtd)|(RADHI)')
    if RADHI.search(news):
        return ('RADHI')

    # Regular Expression for RJM
    RJM = re.compile(r'(Raghupati\sJute\sMills\sLimited)|(RJM)')
    if RJM.search(news):
        return ('RJM')

    # Regular Expression for RBCL
    RBCL = re.compile(r'(Rastriya\sBeema\sCompany\sLimited)|(RBCL)')
    if RBCL.search(news):
        return ('RBCL')

    # Regular Expression for RLFL
    RLFL = re.compile(r'(Reliance\sFinance\sLtd)|(RLFL)')
    if RLFL.search(news):
        return ('RLFL')

    # Regular Expression for RHPC
    RHPC = re.compile(r'(Ridi\sHydropower\sDevelopment\sCompany\sLtd)|(RHPC)')
    if RHPC.search(news):
        return ('RHPC')

    # Regular Expression for RSDC
    RSDC = re.compile(r'(RSDC\sLaghubitta\sBittiya\sSanstha\sLtd)|(RSDC)')
    if RSDC.search(news):
        return ('RSDC')

    # Regular Expression for RMDC
    RMDC = re.compile(r'(Rural\sMicrofinance\sDevelopment\sCentre\sLtd)|(RMDC)')
    if RMDC.search(news):
        return ('RMDC')

    # Regular Expression for SIC
    SIC = re.compile(r'(Sagarmatha\sInsurance\sCo\sLtd)|(SIC)')
    if SIC.search(news):
        return ('SIC')

    # Regular Expression for SHBL
    SHBL = re.compile(r'(Sahara\sBikas\sBank\sLtd)|(SHBL)')
    if SHBL.search(news):
        return ('SHBL')

    # Regular Expression for SBBLJ
    SBBLJ = re.compile(r'(Sahayogi\sBikas\sBank\sLimited)|(SBBLJ)')
    if SBBLJ.search(news):
        return ('SBBLJ')

    # Regular Expression for STC
    STC = re.compile(r'(Salt\sTrading\sCorporation)|(STC)')
    if STC.search(news):
        return ('STC')

    # Regular Expression for SMATA
    SMATA = re.compile(r'(Samata\sMicrofinance\sBittiya\sSanstha\sLtd)|(SMATA)')
    if SMATA.search(news):
        return ('SMATA')

    # Regular Expression for SFC
    SFC = re.compile(r'(Samjhana\sFinance\sCo\sLtd)|(SFC)')
    if SFC.search(news):
        return ('SFC')

    # Regular Expression for SKBBL
    SKBBL = re.compile(r'(Sana\sKisan\sBikas\sBank\sLtd)|(SKBBL)')
    if SKBBL.search(news):
        return ('SKBBL')

    # Regular Expression for SANIMA
    SANIMA = re.compile(r'(Sanima\sBank\sLimited)|(SANIMA)')
    if SANIMA.search(news):
        return ('SANIMA')

    # Regular Expression for SAEF
    SAEF = re.compile(r'(Sanima\sEquity\sFund)|(SAEF)')
    if SAEF.search(news):
        return ('SAEF')

    # Regular Expression for SHPC
    SHPC = re.compile(r'(Sanima\sMai\sHydropower\sLtd)|(SHPC)')
    if SHPC.search(news):
        return ('SHPC')

    # Regular Expression for SKDBL
    SKDBL = re.compile(r'(Saptakoshi\sDevelopment\sBank\sLtd)|(SKDBL)')
    if SKDBL.search(news):
        return ('SKDBL')

    # Regular Expression for SADBL
    SADBL = re.compile(r'(Shangrila\sDevelopment\sBank\sLtd)|(SADBL)')
    if SADBL.search(news):
        return ('SADBL')

    # Regular Expression for SICL
    SICL = re.compile(r'(Shikhar\sInsurance\sCo\sLtd)|(SICL)')
    if SICL.search(news):
        return ('SICL')

    # Regular Expression for SHINE
    SHINE = re.compile(r'(Shine\sResunga\sDevelopment\sBank\sLtd)|(SHINE)')
    if SHINE.search(news):
        return ('SHINE')

    # Regular Expression for SBPP
    SBPP = re.compile(r'(Shree\sBhrikuti\sPulp\sAnd\sPaper\sLimited)|(SBPP)')
    if SBPP.search(news):
        return ('SBPP')

    # Regular Expression for SIFC
    SIFC = re.compile(r'(Shree\sInvestment\sFinance\sCo\sLtd)|(SIFC)')
    if SIFC.search(news):
        return ('SIFC')

    # Regular Expression for SRS
    SRS = re.compile(r'(Shree\sRam\sSugar\sMills\sLimited)|(SRS)')
    if SRS.search(news):
        return ('SRS')

    # Regular Expression for SFFIL
    SFFIL = re.compile(r'(Shrijana\sFinance\sBittaya\sSanstha)|(SFFIL)')
    if SFFIL.search(news):
        return ('SFFIL')

    # Regular Expression for SBL
    SBL = re.compile(r'(Siddhartha\sBank\sLimited)|(SBL)')
    if SBL.search(news):
        return ('SBL')

    # Regular Expression for SEF
    SEF = re.compile(r'(Siddhartha\sEquity\sFund)|(SEF)')
    if SEF.search(news):
        return ('SEF')

    # Regular Expression for SEOS
    SEOS = re.compile(r'(Siddhartha\sEquity\sOrineted\sScheme)|(SEOS)')
    if SEOS.search(news):
        return ('SEOS')

    # Regular Expression for SIL
    SIL = re.compile(r'(Siddhartha\sInsurance\sLtd)|(SIL)')
    if SIL.search(news):
        return ('SIL')

    # Regular Expression for SINDU
    SINDU = re.compile(r'(Sindhu\sBikash\sBank\sLtd)|(SINDU)')
    if SINDU.search(news):
        return ('SINDU')

    # Regular Expression for SHL
    SHL = re.compile(r'(Soaltee\sHotel\sLimited)|(SHL)')
    if SHL.search(news):
        return ('SHL')

    # Regular Expression for SCB
    SCB = re.compile(r'(Standard\sChartered\sBank\sLimited)|(SCB)')
    if SCB.search(news):
        return ('SCB')

    # Regular Expression for SMFDB
    SMFDB = re.compile(r'(Summit\sMicro\sFinance\sDevelopment\sBank\sLtd)|(SMFDB)')
    if SMFDB.search(news):
        return ('SMFDB')

    # Regular Expression for SRBL
    SRBL = re.compile(r'(Sunrise\sBank\sLimited)|(SRBL)')
    if SRBL.search(news):
        return ('SRBL')

    # Regular Expression for SMB
    SMB = re.compile(r'(Support\sMicrofinance\sBittiya\sSanstha\sLtd)|(SMB)')
    if SMB.search(news):
        return ('SMB')

    # Regular Expression for SLICL
    SLICL = re.compile(r'(Surya\sLife\sInsurance\sCompany\sLimited)|(SLICL)')
    if SLICL.search(news):
        return ('SLICL')

    # Regular Expression for SLBS
    SLBS = re.compile(r'(Suryodaya\sLaghubitta\sBittiya\sSanstha\sLtd)|(SLBS)')
    if SLBS.search(news):
        return ('SLBS')

    # Regular Expression for SWBBL
    SWBBL = re.compile(r'(Swabalamban\sLaghubitta\sBittiya\sSanstha\sLimited)|(SWBBL)')
    if SWBBL.search(news):
        return ('SWBBL')

    # Regular Expression for SDESI
    SDESI = re.compile(r'(Swadeshi\sLaghubitta\sBittiya\sSanstha\sLtd)|(SDESI)')
    if SDESI.search(news):
        return ('SDESI')

    # Regular Expression for SLBBL
    SLBBL = re.compile(r'(Swarojgar\sLaghu\sBitta\sBikas\sBank\sLtd)|(SLBBL)')
    if SLBBL.search(news):
        return ('SLBBL')

    # Regular Expression for SYFL
    SYFL = re.compile(r'(Synergy\sFinance\sLtd)|(SYFL)')
    if SYFL.search(news):
        return ('SYFL')

    # Regular Expression for SPDL
    SPDL = re.compile(r'(Synergy\sPower\sDevelopment\sLtd)|(SPDL)')
    if SPDL.search(news):
        return ('SPDL')

    # Regular Expression for TRH
    TRH = re.compile(r'(Taragaon\sRegency\sHotel\sLimited)|(TRH)')
    if TRH.search(news):
        return ('TRH')

    # Regular Expression for TNBL
    TNBL = re.compile(r'(Tinau\sDevelopment\sBank\sLimited)|(TNBL)')
    if TNBL.search(news):
        return ('TNBL')

    # Regular Expression for TDBL
    TDBL = re.compile(r'(Tourism\sDevelopment\sBank\sLimited)|(TDBL)')
    if TDBL.search(news):
        return ('TDBL')

    # Regular Expression for UNL
    UNL = re.compile(r'(Uniliver\sNepal\sLimited)|(UNL)')
    if UNL.search(news):
        return ('UNL')

    # Regular Expression for UFL
    UFL = re.compile(r'(United\sFinance\sLtd)|(UFL)')
    if UFL.search(news):
        return ('UFL')

    # Regular Expression for UIC
    UIC = re.compile(r'(United\sInsurance\sCo\sNepal\sLtd)|(UIC)')
    if UIC.search(news):
        return ('UIC')

    # Regular Expression for UMHL
    UMHL = re.compile(r'(United\sModi\sHydropower\sLtd)|(UMHL)')
    if UMHL.search(news):
        return ('UMHL')

    # Regular Expression for UMB
    UMB = re.compile(r'(Unnati\sMicorfinance\sBittiya\sSanstha\sLtd)|(UMB)')
    if UMB.search(news):
        return ('UMB')

    # Regular Expression for VLBS
    VLBS = re.compile(r'(Vijaya\slaghubitta\sBittiya\sSanstha\sLtd)|(VLBS)')
    if VLBS.search(news):
        return ('VLBS')

    # Regular Expression for WDBL
    WDBL = re.compile(r'(Western\sDevelopment\sBank\sLimited)|(WDBL)')
    if WDBL.search(news):
        return ('WDBL')

    # Regular Expression for WOMI
    WOMI = re.compile(r'(Womi\sMicrofinance\sBittiya\sSanstha\sLtd)|(WOMI)')
    if WOMI.search(news):
        return ('WOMI')

    # Regular Expression for WMBF
    WMBF = re.compile(r'(World\sMerchant\sBanking\sFinance\sLtd)|(WMBF)')
    if WMBF.search(news):
        return ('WMBF')

    # Regular Expression for YHL
    YHL = re.compile(r'(Yak\sAnd\sYeti\sHotel\sLimited)|(YHL)')
    if YHL.search(news):
        return ('YHL')


# print(classifier(n))
