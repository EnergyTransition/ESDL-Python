<?xml version="1.0" encoding="UTF-8"?>
<esdl:EnergySystem xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:esdl="http://www.tno.nl/esdl/180901"
xsi:schemaLocation="http://www.tno.nl/esdl/180901 ../esdl/model/esdl.ecore" name="My EnergySystem">
    <esdl:instance name="First instance">
        <esdl:area name="area">
            <esdl:WindTurbine name="WindTurbine" power="3.000000e+06">
                <esdl:OutPort id="8084f026-dc76-4d56-afc2-e5c34ba9c55c"/>
            </esdl:WindTurbine>
            <esdl:AggregatedBuilding name="Aggregated households">
                <esdl:ElectricityDemand name="ElectricityDemand">
                    <esdl:InPort id="fed1793b-5ddd-42ee-a0d4-50d671aedd7e"/>
                </esdl:ElectricityDemand>
            </esdl:AggregatedBuilding>
            <esdl:ElectricityNetwork>
                <esdl:InPort id="ddcc05a8-c24c-49a5-a849-253cd626f873" connectedTo="8084f026-dc76-4d56-afc2-e5c34ba9c55c"/>
                <esdl:OutPort id="41f066c4-ed2a-4efa-b735-349ef1be1037" connectedTo="fed1793b-5ddd-42ee-a0d4-50d671aedd7e"/>
            </esdl:ElectricityNetwork>
        </esdl:area>
    </esdl:instance>
</esdl:EnergySystem>
