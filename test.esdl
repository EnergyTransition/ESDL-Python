<?xml version="1.0" encoding="UTF-8"?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:esdl="http://www.tno.nl/esdl"
xsi:schemaLocation="http://www.tno.nl/esdl ../esdl/model/esdl.ecore" name="My EnergySystem">
    <esdl:instance xmlns:esdl="http://www.tno.nl/esdl" name="First instance">
        <esdl:area xmlns:esdl="http://www.tno.nl/esdl" name="City">
            <esdl:asset name="WindTurbine" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:WindTurbine" power="3.000000e+06">
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="d70abcca-f396-495c-82e5-fb070138c26d" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="24a31625-4a60-4e66-881d-49f824af2e6a"/>
            </esdl:asset>
            <esdl:asset name="Aggregated households" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:AggregatedBuilding">
                <esdl:asset name="ElectricityDemand" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityDemand">
                    <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="87cb0c5d-55d5-4901-bb66-870bb3ad9628" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="31acced7-a2a3-498e-b556-be07e2be8137"/>
                </esdl:asset>
            </esdl:asset>
            <esdl:asset name="Electricity Network" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityNetwork">
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="24a31625-4a60-4e66-881d-49f824af2e6a" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="d70abcca-f396-495c-82e5-fb070138c26d"/>
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="31acced7-a2a3-498e-b556-be07e2be8137" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="87cb0c5d-55d5-4901-bb66-870bb3ad9628"/>
</esdl:asset>
        </esdl:area>
    </esdl:instance>
</esdl:EnergySystem>
