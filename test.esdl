<?xml version="1.0" encoding="UTF-8"?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:esdl="http://www.tno.nl/esdl"
xsi:schemaLocation="http://www.tno.nl/esdl ../esdl/model/esdl.ecore" name="My EnergySystem">
    <esdl:instance xmlns:esdl="http://www.tno.nl/esdl" name="First instance">
        <esdl:area xmlns:esdl="http://www.tno.nl/esdl" name="City">
            <esdl:asset name="WindTurbine" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:WindTurbine" power="3.000000e+06">
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="33952f43-bb71-463f-af1d-e49ab6db048b" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="6c7a81ca-620d-4b44-8410-3edcb6d8e693"/>
            </esdl:asset>
            <esdl:asset name="Aggregated households" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:AggregatedBuilding">
                <esdl:asset name="ElectricityDemand" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityDemand">
                    <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="f14ac0c1-6688-4223-b5a3-45d2d21ff7c9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="d9036d29-b81b-466e-80a9-2378d3571029"/>
                </esdl:asset>
            </esdl:asset>
            <esdl:asset name="Electricity Network" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:ElectricityNetwork">
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="6c7a81ca-620d-4b44-8410-3edcb6d8e693" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:InPort" connectedTo="33952f43-bb71-463f-af1d-e49ab6db048b"/>
                <esdl:port xmlns:esdl="http://www.tno.nl/esdl" id="d9036d29-b81b-466e-80a9-2378d3571029" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="esdl:OutPort" connectedTo="f14ac0c1-6688-4223-b5a3-45d2d21ff7c9"/>
</esdl:asset>
        </esdl:area>
    </esdl:instance>
</esdl:EnergySystem>
