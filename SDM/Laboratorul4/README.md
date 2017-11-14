Key Page : PD166
Descriptor :
<layout code="PD166" style="TestoCombo" description="ATM9 - Ripristino eccedenze ATM anni precedenti da A9ECCXXXX">

    <hidden name="AVERE" value="A9CECATM"/>

    <combo name="DARE" label="Scegliere dalla lista il conto da addebitare (DARE) *" mandatory="true" >
      <option label="A9ECC2011" value="A9ECC2011" />
      <option label="A9ECC2012" value="A9ECC2012" />
      <option label="A9ECC2013" value="A9ECC2013" />
      <option label="A9ECC2014" value="A9ECC2014" />
      <option label="A9ECC2015" value="A9ECC2015" />
      <option label="A9ECC2016" value="A9ECC2016" />
      <option label="A9ECC2017" value="A9ECC2017" />
      <option label="A9ECC2018" value="A9ECC2018" />
      <option label="A9ECC2019" value="A9ECC2019" />
      <option label="A9ECC2020" value="A9ECC2020" />
      <option label="A9ECC2021" value="A9ECC2021" />
   </combo>

    <free name="CausaleVariabile" label="Causale Variabile*" mandatory="true"/>

    <free name="succursale" label="Codice Succursale*" exitKey="cdrLid" handler="it.sella.conti.commons.blindature.handlers.GetCDRFromSucc" />

    <free name="importo" label="Importo - EUR *"/>
    <hidden name="divisa" value="EUR" />
    <virtual name="importo,divisa" handler="it.sella.conti.commons.blindature.handlers.ImportoChecker" />

    <freedate name="ValutaAccredito" exitKey="dataValutaAccredito" label="Valuta (gg/mm/aaaa) *"
     handler="it.sella.conti.commons.blindature.handlers.DateHandler" extraInfo="true"/>
    <virtual name="dataValutaAccredito,importo" stepKey="needMoreSecurity"
     handler="it.sella.conti.commons.blindature.handlers.ForzaturaValutaStandardHandler"/>

    <hidden name="checkSeContoCassa" value="okCassa" />
    <virtual name="contoCassa,checkSeContoCassa" exitKey="causIntAvere" handler="it.sella.conti.commons.blindature.handlers.OnCompareSwitchValueHandler"
     extraInfo="00005037,00005036" />

            <script><![CDATA[
            document.dealerCCDR.importo.focus();
            ]]></script>

</layout>