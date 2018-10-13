#!/usr/bin/env python

#
# Generated Sat Oct 13 17:09:52 2018 by generateDS.py version 2.29.24.
# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'esdl_sup.py')
#   ('-s', 'esdl_sub.py')
#   ('--no-namespace-defs', '')
#   ('--root-element', 'EnergySystem')
#   ('--export', 'write etree')
#
# Command line arguments:
#   esdlXML.xsd
#
# Command line:
#   C:\Users\matthijssenef\AppData\Local\Programs\Python\Python37\Scripts\generateDS -o "esdl_sup.py" -s "esdl_sub.py" --no-namespace-defs --root-element="EnergySystem" --export="write etree" esdlXML.xsd
#
# Current working directory (os.getcwd()):
#   model
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class EnergySystemSub(supermod.EnergySystem):
    def __init__(self, name=None, description=None, geographicalScope=None, sector=None, measures=None, instance=None, potentials=None, energySystemInformation=None, parties=None, services=None):
        super(EnergySystemSub, self).__init__(name, description, geographicalScope, sector, measures, instance, potentials, energySystemInformation, parties, services, )
supermod.EnergySystem.subclass = EnergySystemSub
# end class EnergySystemSub


class AreaSub(supermod.Area):
    def __init__(self, id=None, name=None, scope='UNDEFINED', type_=None, geometryReference=None, buildingDensity=None, potentials=None, containingArea=None, isOwnedBy=None, location=None, contour=None, socialProperties=None, economicProperties=None, asset=None, area=None, mobilityProperties=None, kpiList=None):
        super(AreaSub, self).__init__(id, name, scope, type_, geometryReference, buildingDensity, potentials, containingArea, isOwnedBy, location, contour, socialProperties, economicProperties, asset, area, mobilityProperties, kpiList, )
supermod.Area.subclass = AreaSub
# end class AreaSub


class PortSub(supermod.Port):
    def __init__(self, id=None, maxPower=None, energyasset=None, carrier=None, profile=None, extensiontype_=None):
        super(PortSub, self).__init__(id, maxPower, energyasset, carrier, profile, extensiontype_, )
supermod.Port.subclass = PortSub
# end class PortSub


class InPortSub(supermod.InPort):
    def __init__(self, id=None, maxPower=None, energyasset=None, carrier=None, profile=None, connectedTo=None):
        super(InPortSub, self).__init__(id, maxPower, energyasset, carrier, profile, connectedTo, )
supermod.InPort.subclass = InPortSub
# end class InPortSub


class OutPortSub(supermod.OutPort):
    def __init__(self, id=None, maxPower=None, energyasset=None, carrier=None, profile=None, connectedTo=None):
        super(OutPortSub, self).__init__(id, maxPower, energyasset, carrier, profile, connectedTo, )
supermod.OutPort.subclass = OutPortSub
# end class OutPortSub


class EconomicPropertiesSub(supermod.EconomicProperties):
    def __init__(self, averageIncome=None, averageWOZvalue=None, percentageOwnerOccupiedProperties=None, percentageHousingAssociation=None, percentagePrivateRental=None):
        super(EconomicPropertiesSub, self).__init__(averageIncome, averageWOZvalue, percentageOwnerOccupiedProperties, percentageHousingAssociation, percentagePrivateRental, )
supermod.EconomicProperties.subclass = EconomicPropertiesSub
# end class EconomicPropertiesSub


class SocialPropertiesSub(supermod.SocialProperties):
    def __init__(self, socialCohesion=None, populationDensity=None, numberOfInhabitants=None):
        super(SocialPropertiesSub, self).__init__(socialCohesion, populationDensity, numberOfInhabitants, )
supermod.SocialProperties.subclass = SocialPropertiesSub
# end class SocialPropertiesSub


class ItemSub(supermod.Item):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, extensiontype_=None):
        super(ItemSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, extensiontype_, )
supermod.Item.subclass = ItemSub
# end class ItemSub


class MeasuresSub(supermod.Measures):
    def __init__(self, asset=None):
        super(MeasuresSub, self).__init__(asset, )
supermod.Measures.subclass = MeasuresSub
# end class MeasuresSub


class InstanceSub(supermod.Instance):
    def __init__(self, id=None, name=None, description=None, detailLevel='UNDEFINED', aggrType=None, date=None, area=None):
        super(InstanceSub, self).__init__(id, name, description, detailLevel, aggrType, date, area, )
supermod.Instance.subclass = InstanceSub
# end class InstanceSub


class ServiceSub(supermod.Service):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, extensiontype_=None):
        super(ServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, extensiontype_, )
supermod.Service.subclass = ServiceSub
# end class ServiceSub


class PotentialSub(supermod.Potential):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, extensiontype_=None):
        super(PotentialSub, self).__init__(id, name, areas, asset, geometry, dataSource, extensiontype_, )
supermod.Potential.subclass = PotentialSub
# end class PotentialSub


class WindPotentialSub(supermod.WindPotential):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, windspeed=None, height=None):
        super(WindPotentialSub, self).__init__(id, name, areas, asset, geometry, dataSource, windspeed, height, )
supermod.WindPotential.subclass = WindPotentialSub
# end class WindPotentialSub


class PotentialsSub(supermod.Potentials):
    def __init__(self, potential=None):
        super(PotentialsSub, self).__init__(potential, )
supermod.Potentials.subclass = PotentialsSub
# end class PotentialsSub


class CarriersSub(supermod.Carriers):
    def __init__(self, carrier=None, dataSource=None):
        super(CarriersSub, self).__init__(carrier, dataSource, )
supermod.Carriers.subclass = CarriersSub
# end class CarriersSub


class EnergySystemInformationSub(supermod.EnergySystemInformation):
    def __init__(self, carriers=None, profiles=None, dataSources=None, mobilityFuelInformation=None, quantityAndUnitList=None):
        super(EnergySystemInformationSub, self).__init__(carriers, profiles, dataSources, mobilityFuelInformation, quantityAndUnitList, )
supermod.EnergySystemInformation.subclass = EnergySystemInformationSub
# end class EnergySystemInformationSub


class GenericProfileSub(supermod.GenericProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, extensiontype_=None):
        super(GenericProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, extensiontype_, )
supermod.GenericProfile.subclass = GenericProfileSub
# end class GenericProfileSub


class StaticProfileSub(supermod.StaticProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, extensiontype_=None):
        super(StaticProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, extensiontype_, )
supermod.StaticProfile.subclass = StaticProfileSub
# end class StaticProfileSub


class DateTimeProfileSub(supermod.DateTimeProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, element=None):
        super(DateTimeProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, element, )
supermod.DateTimeProfile.subclass = DateTimeProfileSub
# end class DateTimeProfileSub


class ProfileElementSub(supermod.ProfileElement):
    def __init__(self, from_=None, to=None, value=None):
        super(ProfileElementSub, self).__init__(from_, to, value, )
supermod.ProfileElement.subclass = ProfileElementSub
# end class ProfileElementSub


class ExternalProfileSub(supermod.ExternalProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, extensiontype_=None):
        super(ExternalProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, extensiontype_, )
supermod.ExternalProfile.subclass = ExternalProfileSub
# end class ExternalProfileSub


class SingleValueSub(supermod.SingleValue):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, value=None):
        super(SingleValueSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, value, )
supermod.SingleValue.subclass = SingleValueSub
# end class SingleValueSub


class GenericDistributionSub(supermod.GenericDistribution):
    def __init__(self, name=None, extensiontype_=None):
        super(GenericDistributionSub, self).__init__(name, extensiontype_, )
supermod.GenericDistribution.subclass = GenericDistributionSub
# end class GenericDistributionSub


class PercentileSub(supermod.Percentile):
    def __init__(self, percentile=None, value=None):
        super(PercentileSub, self).__init__(percentile, value, )
supermod.Percentile.subclass = PercentileSub
# end class PercentileSub


class PercentileDistributionSub(supermod.PercentileDistribution):
    def __init__(self, name=None, percentile=None):
        super(PercentileDistributionSub, self).__init__(name, percentile, )
supermod.PercentileDistribution.subclass = PercentileDistributionSub
# end class PercentileDistributionSub


class CostInformationSub(supermod.CostInformation):
    def __init__(self, investmentCosts=None, installationCosts=None, O_and_MCosts=None):
        super(CostInformationSub, self).__init__(investmentCosts, installationCosts, O_and_MCosts, )
supermod.CostInformation.subclass = CostInformationSub
# end class CostInformationSub


class LabelDistributionSub(supermod.LabelDistribution):
    def __init__(self, name=None, extensiontype_=None):
        super(LabelDistributionSub, self).__init__(name, extensiontype_, )
supermod.LabelDistribution.subclass = LabelDistributionSub
# end class LabelDistributionSub


class StringLabelDistributionSub(supermod.StringLabelDistribution):
    def __init__(self, name=None, stringPerc=None):
        super(StringLabelDistributionSub, self).__init__(name, stringPerc, )
supermod.StringLabelDistribution.subclass = StringLabelDistributionSub
# end class StringLabelDistributionSub


class EnergyLabelDistributionSub(supermod.EnergyLabelDistribution):
    def __init__(self, name=None, labelPerc=None):
        super(EnergyLabelDistributionSub, self).__init__(name, labelPerc, )
supermod.EnergyLabelDistribution.subclass = EnergyLabelDistributionSub
# end class EnergyLabelDistributionSub


class StringPercSub(supermod.StringPerc):
    def __init__(self, label=None, percentage=None):
        super(StringPercSub, self).__init__(label, percentage, )
supermod.StringPerc.subclass = StringPercSub
# end class StringPercSub


class EnergyLabelPercSub(supermod.EnergyLabelPerc):
    def __init__(self, energyLabel=None, percentage=None):
        super(EnergyLabelPercSub, self).__init__(energyLabel, percentage, )
supermod.EnergyLabelPerc.subclass = EnergyLabelPercSub
# end class EnergyLabelPercSub


class FromToDistributionSub(supermod.FromToDistribution):
    def __init__(self, name=None, fromToPerc=None):
        super(FromToDistributionSub, self).__init__(name, fromToPerc, )
supermod.FromToDistribution.subclass = FromToDistributionSub
# end class FromToDistributionSub


class FromToPercSub(supermod.FromToPerc):
    def __init__(self, from_=None, to=None, percentage=None):
        super(FromToPercSub, self).__init__(from_, to, percentage, )
supermod.FromToPerc.subclass = FromToPercSub
# end class FromToPercSub


class PItemStatSub(supermod.PItemStat):
    def __init__(self, value=None, sigma=None):
        super(PItemStatSub, self).__init__(value, sigma, )
supermod.PItemStat.subclass = PItemStatSub
# end class PItemStatSub


class AbstractVarianceSub(supermod.AbstractVariance):
    def __init__(self, extensiontype_=None):
        super(AbstractVarianceSub, self).__init__(extensiontype_, )
supermod.AbstractVariance.subclass = AbstractVarianceSub
# end class AbstractVarianceSub


class SymetricVarianceSub(supermod.SymetricVariance):
    def __init__(self, sigma=None):
        super(SymetricVarianceSub, self).__init__(sigma, )
supermod.SymetricVariance.subclass = SymetricVarianceSub
# end class SymetricVarianceSub


class AssymetricVarianceSub(supermod.AssymetricVariance):
    def __init__(self, sigmaMin=None, sigmaPlus=None):
        super(AssymetricVarianceSub, self).__init__(sigmaMin, sigmaPlus, )
supermod.AssymetricVariance.subclass = AssymetricVarianceSub
# end class AssymetricVarianceSub


class DoubleAssymetricVarianceSub(supermod.DoubleAssymetricVariance):
    def __init__(self, plus34perc=None, plus48perc=None, min34perc=None, min48perc=None):
        super(DoubleAssymetricVarianceSub, self).__init__(plus34perc, plus48perc, min34perc, min48perc, )
supermod.DoubleAssymetricVariance.subclass = DoubleAssymetricVarianceSub
# end class DoubleAssymetricVarianceSub


class PartySub(supermod.Party):
    def __init__(self, id=None, name=None, shortName=None, owns=None, ownsArea=None):
        super(PartySub, self).__init__(id, name, shortName, owns, ownsArea, )
supermod.Party.subclass = PartySub
# end class PartySub


class URIProfileSub(supermod.URIProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, URI=None):
        super(URIProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, URI, )
supermod.URIProfile.subclass = URIProfileSub
# end class URIProfileSub


class DatabaseProfileSub(supermod.DatabaseProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, host=None, port=None, database=None, filters=None, extensiontype_=None):
        super(DatabaseProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, host, port, database, filters, extensiontype_, )
supermod.DatabaseProfile.subclass = DatabaseProfileSub
# end class DatabaseProfileSub


class InfluxDBProfileSub(supermod.InfluxDBProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, host=None, port=None, database=None, filters=None, measurement=None, field=None):
        super(InfluxDBProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, host, port, database, filters, measurement, field, )
supermod.InfluxDBProfile.subclass = InfluxDBProfileSub
# end class InfluxDBProfileSub


class GeometrySub(supermod.Geometry):
    def __init__(self, extensiontype_=None):
        super(GeometrySub, self).__init__(extensiontype_, )
supermod.Geometry.subclass = GeometrySub
# end class GeometrySub


class CarrierSub(supermod.Carrier):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, extensiontype_=None):
        super(CarrierSub, self).__init__(name, id, cost, dataSource, extensiontype_, )
supermod.Carrier.subclass = CarrierSub
# end class CarrierSub


class RangeSub(supermod.Range):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, minValue=None, maxValue=None):
        super(RangeSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, minValue, maxValue, )
supermod.Range.subclass = RangeSub
# end class RangeSub


class SolarFieldPotentialSub(supermod.SolarFieldPotential):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, solarIrradiance=None):
        super(SolarFieldPotentialSub, self).__init__(id, name, areas, asset, geometry, dataSource, solarIrradiance, )
supermod.SolarFieldPotential.subclass = SolarFieldPotentialSub
# end class SolarFieldPotentialSub


class DurationSub(supermod.Duration):
    def __init__(self, value=None, durationUnit='SECOND'):
        super(DurationSub, self).__init__(value, durationUnit, )
supermod.Duration.subclass = DurationSub
# end class DurationSub


class ProfileReferenceSub(supermod.ProfileReference):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1, reference=None):
        super(ProfileReferenceSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, reference, )
supermod.ProfileReference.subclass = ProfileReferenceSub
# end class ProfileReferenceSub


class ProfilesSub(supermod.Profiles):
    def __init__(self, profile=None):
        super(ProfilesSub, self).__init__(profile, )
supermod.Profiles.subclass = ProfilesSub
# end class ProfilesSub


class PartiesSub(supermod.Parties):
    def __init__(self, party=None):
        super(PartiesSub, self).__init__(party, )
supermod.Parties.subclass = PartiesSub
# end class PartiesSub


class DataSourcesSub(supermod.DataSources):
    def __init__(self, dataSource=None):
        super(DataSourcesSub, self).__init__(dataSource, )
supermod.DataSources.subclass = DataSourcesSub
# end class DataSourcesSub


class ResidualHeatSourcePotentialSub(supermod.ResidualHeatSourcePotential):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, power=None):
        super(ResidualHeatSourcePotentialSub, self).__init__(id, name, areas, asset, geometry, dataSource, power, )
supermod.ResidualHeatSourcePotential.subclass = ResidualHeatSourcePotentialSub
# end class ResidualHeatSourcePotentialSub


class SubPolygonSub(supermod.SubPolygon):
    def __init__(self, point=None):
        super(SubPolygonSub, self).__init__(point, )
supermod.SubPolygon.subclass = SubPolygonSub
# end class SubPolygonSub


class MultiPolygonSub(supermod.MultiPolygon):
    def __init__(self, polygon=None):
        super(MultiPolygonSub, self).__init__(polygon, )
supermod.MultiPolygon.subclass = MultiPolygonSub
# end class MultiPolygonSub


class MobilityFuelInformationSub(supermod.MobilityFuelInformation):
    def __init__(self, vehicleFuelEfficiency=None, dataSource=None):
        super(MobilityFuelInformationSub, self).__init__(vehicleFuelEfficiency, dataSource, )
supermod.MobilityFuelInformation.subclass = MobilityFuelInformationSub
# end class MobilityFuelInformationSub


class VehicleFuelEfficiencySub(supermod.VehicleFuelEfficiency):
    def __init__(self, vehicleType=None, fuel=None, efficiency=None):
        super(VehicleFuelEfficiencySub, self).__init__(vehicleType, fuel, efficiency, )
supermod.VehicleFuelEfficiency.subclass = VehicleFuelEfficiencySub
# end class VehicleFuelEfficiencySub


class MobilityPropertiesSub(supermod.MobilityProperties):
    def __init__(self, numberOfVehicles=None):
        super(MobilityPropertiesSub, self).__init__(numberOfVehicles, )
supermod.MobilityProperties.subclass = MobilityPropertiesSub
# end class MobilityPropertiesSub


class NumberOfVehiclesSub(supermod.NumberOfVehicles):
    def __init__(self, vehicleCount=None):
        super(NumberOfVehiclesSub, self).__init__(vehicleCount, )
supermod.NumberOfVehicles.subclass = NumberOfVehiclesSub
# end class NumberOfVehiclesSub


class VehicleCountSub(supermod.VehicleCount):
    def __init__(self, type_=None, count=None):
        super(VehicleCountSub, self).__init__(type_, count, )
supermod.VehicleCount.subclass = VehicleCountSub
# end class VehicleCountSub


class ServicesSub(supermod.Services):
    def __init__(self, service=None):
        super(ServicesSub, self).__init__(service, )
supermod.Services.subclass = ServicesSub
# end class ServicesSub


class AbstractDataSourceSub(supermod.AbstractDataSource):
    def __init__(self, extensiontype_=None):
        super(AbstractDataSourceSub, self).__init__(extensiontype_, )
supermod.AbstractDataSource.subclass = AbstractDataSourceSub
# end class AbstractDataSourceSub


class DataSourceReferenceSub(supermod.DataSourceReference):
    def __init__(self, reference=None):
        super(DataSourceReferenceSub, self).__init__(reference, )
supermod.DataSourceReference.subclass = DataSourceReferenceSub
# end class DataSourceReferenceSub


class KPIListSub(supermod.KPIList):
    def __init__(self, description=None, kpi=None):
        super(KPIListSub, self).__init__(description, kpi, )
supermod.KPIList.subclass = KPIListSub
# end class KPIListSub


class KPISub(supermod.KPI):
    def __init__(self, name=None, value=None, quantityAndUnit=None):
        super(KPISub, self).__init__(name, value, quantityAndUnit, )
supermod.KPI.subclass = KPISub
# end class KPISub


class QuantityAndUnitListSub(supermod.QuantityAndUnitList):
    def __init__(self, quantityAndUnit=None):
        super(QuantityAndUnitListSub, self).__init__(quantityAndUnit, )
supermod.QuantityAndUnitList.subclass = QuantityAndUnitListSub
# end class QuantityAndUnitListSub


class AbstractQuantityAndUnitSub(supermod.AbstractQuantityAndUnit):
    def __init__(self, extensiontype_=None):
        super(AbstractQuantityAndUnitSub, self).__init__(extensiontype_, )
supermod.AbstractQuantityAndUnit.subclass = AbstractQuantityAndUnitSub
# end class AbstractQuantityAndUnitSub


class QuantityAndUnitReferenceSub(supermod.QuantityAndUnitReference):
    def __init__(self, reference=None):
        super(QuantityAndUnitReferenceSub, self).__init__(reference, )
supermod.QuantityAndUnitReference.subclass = QuantityAndUnitReferenceSub
# end class QuantityAndUnitReferenceSub


class QuantityAndUnitTypeSub(supermod.QuantityAndUnitType):
    def __init__(self, physicalQuantity=None, multiplier=None, unit=None, perMultiplier=None, perUnit=None, description=None, perTimeUnit=None, id=None):
        super(QuantityAndUnitTypeSub, self).__init__(physicalQuantity, multiplier, unit, perMultiplier, perUnit, description, perTimeUnit, id, )
supermod.QuantityAndUnitType.subclass = QuantityAndUnitTypeSub
# end class QuantityAndUnitTypeSub


class DataSourceSub(supermod.DataSource):
    def __init__(self, id=None, name=None, description=None, reference=None, attribution=None, releaseDate=None, version=None, licence=None):
        super(DataSourceSub, self).__init__(id, name, description, reference, attribution, releaseDate, version, licence, )
supermod.DataSource.subclass = DataSourceSub
# end class DataSourceSub


class CommoditySub(supermod.Commodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, extensiontype_=None):
        super(CommoditySub, self).__init__(name, id, cost, dataSource, extensiontype_, )
supermod.Commodity.subclass = CommoditySub
# end class CommoditySub


class LineSub(supermod.Line):
    def __init__(self, point=None):
        super(LineSub, self).__init__(point, )
supermod.Line.subclass = LineSub
# end class LineSub


class EnergyCarrierSub(supermod.EnergyCarrier):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, energyContent=0.0, emission=0.0, energyCarrierType=None, stateOfMatter=None, energyContentUnit=None, emissionUnit=None):
        super(EnergyCarrierSub, self).__init__(name, id, cost, dataSource, energyContent, emission, energyCarrierType, stateOfMatter, energyContentUnit, emissionUnit, )
supermod.EnergyCarrier.subclass = EnergyCarrierSub
# end class EnergyCarrierSub


class EnergyServiceSub(supermod.EnergyService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, extensiontype_=None):
        super(EnergyServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, extensiontype_, )
supermod.EnergyService.subclass = EnergyServiceSub
# end class EnergyServiceSub


class LegalAreaSub(supermod.LegalArea):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, purpose=None):
        super(LegalAreaSub, self).__init__(id, name, areas, asset, geometry, dataSource, purpose, )
supermod.LegalArea.subclass = LegalAreaSub
# end class LegalAreaSub


class PolygonSub(supermod.Polygon):
    def __init__(self, exterior=None, interior=None):
        super(PolygonSub, self).__init__(exterior, interior, )
supermod.Polygon.subclass = PolygonSub
# end class PolygonSub


class PointSub(supermod.Point):
    def __init__(self, lat=None, lon=None):
        super(PointSub, self).__init__(lat, lon, )
supermod.Point.subclass = PointSub
# end class PointSub


class GeothermalPotentialSub(supermod.GeothermalPotential):
    def __init__(self, id=None, name=None, areas=None, asset=None, geometry=None, dataSource=None, temperature=None, depth=None, potential=None, powerPerDoublet='UNKNOWN'):
        super(GeothermalPotentialSub, self).__init__(id, name, areas, asset, geometry, dataSource, temperature, depth, potential, powerPerDoublet, )
supermod.GeothermalPotential.subclass = GeothermalPotentialSub
# end class GeothermalPotentialSub


class AssetSub(supermod.Asset):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, extensiontype_=None):
        super(AssetSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, extensiontype_, )
supermod.Asset.subclass = AssetSub
# end class AssetSub


class EnergyAssetSub(supermod.EnergyAsset):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, extensiontype_=None):
        super(EnergyAssetSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, extensiontype_, )
supermod.EnergyAsset.subclass = EnergyAssetSub
# end class EnergyAssetSub


class ControlStrategySub(supermod.ControlStrategy):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, extensiontype_=None):
        super(ControlStrategySub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, extensiontype_, )
supermod.ControlStrategy.subclass = ControlStrategySub
# end class ControlStrategySub


class EnergyCommoditySub(supermod.EnergyCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None):
        super(EnergyCommoditySub, self).__init__(name, id, cost, dataSource, )
supermod.EnergyCommodity.subclass = EnergyCommoditySub
# end class EnergyCommoditySub


class ElectricityCommoditySub(supermod.ElectricityCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, voltage=None):
        super(ElectricityCommoditySub, self).__init__(name, id, cost, dataSource, voltage, )
supermod.ElectricityCommodity.subclass = ElectricityCommoditySub
# end class ElectricityCommoditySub


class HeatCommoditySub(supermod.HeatCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, temperature=None):
        super(HeatCommoditySub, self).__init__(name, id, cost, dataSource, temperature, )
supermod.HeatCommodity.subclass = HeatCommoditySub
# end class HeatCommoditySub


class GasCommoditySub(supermod.GasCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, pressure=None):
        super(GasCommoditySub, self).__init__(name, id, cost, dataSource, pressure, )
supermod.GasCommodity.subclass = GasCommoditySub
# end class GasCommoditySub


class AggregatorServiceSub(supermod.AggregatorService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None):
        super(AggregatorServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, )
supermod.AggregatorService.subclass = AggregatorServiceSub
# end class AggregatorServiceSub


class AbstractBuildingSub(supermod.AbstractBuilding):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, extensiontype_=None):
        super(AbstractBuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, extensiontype_, )
supermod.AbstractBuilding.subclass = AbstractBuildingSub
# end class AbstractBuildingSub


class DemandResponseServiceSub(supermod.DemandResponseService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None):
        super(DemandResponseServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, )
supermod.DemandResponseService.subclass = DemandResponseServiceSub
# end class DemandResponseServiceSub


class InsulationSub(supermod.Insulation):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, thermalInsulation=None):
        super(InsulationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, thermalInsulation, )
supermod.Insulation.subclass = InsulationSub
# end class InsulationSub


class BuildingSub(supermod.Building):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, buildingYear=None, residentialBuildingType=None, floorArea=None, numberOfFloors=None, slantedRoofArea=None, flatRoofArea=None, roofType=None, wallArea=None, windowArea=None, perimeter=None, height=None, rcFloor=None, rcWall=None, rcRoof=None, uWindow=None, orientation=None, glasType=None, ventilationType=None):
        super(BuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, buildingYear, residentialBuildingType, floorArea, numberOfFloors, slantedRoofArea, flatRoofArea, roofType, wallArea, windowArea, perimeter, height, rcFloor, rcWall, rcRoof, uWindow, orientation, glasType, ventilationType, )
supermod.Building.subclass = BuildingSub
# end class BuildingSub


class BuildingUnitSub(supermod.BuildingUnit):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, type_=None, housingType=None, numberOfInhabitants=None, inhabitantsType=None):
        super(BuildingUnitSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, type_, housingType, numberOfInhabitants, inhabitantsType, )
supermod.BuildingUnit.subclass = BuildingUnitSub
# end class BuildingUnitSub


class TransportSub(supermod.Transport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None):
        super(TransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_, )
supermod.Transport.subclass = TransportSub
# end class TransportSub


class ConversionSub(supermod.Conversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, extensiontype_=None):
        super(ConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, extensiontype_, )
supermod.Conversion.subclass = ConversionSub
# end class ConversionSub


class StorageSub(supermod.Storage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None, extensiontype_=None):
        super(StorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, extensiontype_, )
supermod.Storage.subclass = StorageSub
# end class StorageSub


class ConsumerSub(supermod.Consumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', extensiontype_=None):
        super(ConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, extensiontype_, )
supermod.Consumer.subclass = ConsumerSub
# end class ConsumerSub


class ProducerSub(supermod.Producer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, extensiontype_=None):
        super(ProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, extensiontype_, )
supermod.Producer.subclass = ProducerSub
# end class ProducerSub


class DrivenByDemandSub(supermod.DrivenByDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None):
        super(DrivenByDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, )
supermod.DrivenByDemand.subclass = DrivenByDemandSub
# end class DrivenByDemandSub


class GasStorageSub(supermod.GasStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None):
        super(GasStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, )
supermod.GasStorage.subclass = GasStorageSub
# end class GasStorageSub


class MobilityDemandSub(supermod.MobilityDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', fuelType=None, distance=None, efficiency=None, type_=None):
        super(MobilityDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, fuelType, distance, efficiency, type_, )
supermod.MobilityDemand.subclass = MobilityDemandSub
# end class MobilityDemandSub


class FermentationPlantSub(supermod.FermentationPlant):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None):
        super(FermentationPlantSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, )
supermod.FermentationPlant.subclass = FermentationPlantSub
# end class FermentationPlantSub


class ResidualHeatSourceSub(supermod.ResidualHeatSource):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, type_=None):
        super(ResidualHeatSourceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, type_, )
supermod.ResidualHeatSource.subclass = ResidualHeatSourceSub
# end class ResidualHeatSourceSub


class SolarCollectorSub(supermod.SolarCollector):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None):
        super(SolarCollectorSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, )
supermod.SolarCollector.subclass = SolarCollectorSub
# end class SolarCollectorSub


class EnergyDemandSub(supermod.EnergyDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(EnergyDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.EnergyDemand.subclass = EnergyDemandSub
# end class EnergyDemandSub


class EnergyNetworkSub(supermod.EnergyNetwork):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(EnergyNetworkSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.EnergyNetwork.subclass = EnergyNetworkSub
# end class EnergyNetworkSub


class AircoSub(supermod.Airco):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None):
        super(AircoSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, )
supermod.Airco.subclass = AircoSub
# end class AircoSub


class CoolingDemandSub(supermod.CoolingDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(CoolingDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.CoolingDemand.subclass = CoolingDemandSub
# end class CoolingDemandSub


class ValveSub(supermod.Valve):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(ValveSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.Valve.subclass = ValveSub
# end class ValveSub


class PumpSub(supermod.Pump):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(PumpSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.Pump.subclass = PumpSub
# end class PumpSub


class XToPowerSub(supermod.XToPower):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None):
        super(XToPowerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, )
supermod.XToPower.subclass = XToPowerSub
# end class XToPowerSub


class CCSSub(supermod.CCS):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None):
        super(CCSSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, )
supermod.CCS.subclass = CCSSub
# end class CCSSub


class PowerToXSub(supermod.PowerToX):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None):
        super(PowerToXSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, )
supermod.PowerToX.subclass = PowerToXSub
# end class PowerToXSub


class LossesSub(supermod.Losses):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(LossesSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.Losses.subclass = LossesSub
# end class LossesSub


class AggregatedBuildingSub(supermod.AggregatedBuilding):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, numberOfBuildings=None, aggregationOf=None, energyLabelDistribution=None, buildingYearDistribution=None):
        super(AggregatedBuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, numberOfBuildings, aggregationOf, energyLabelDistribution, buildingYearDistribution, )
supermod.AggregatedBuilding.subclass = AggregatedBuildingSub
# end class AggregatedBuildingSub


class EVChargingStationSub(supermod.EVChargingStation):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(EVChargingStationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.EVChargingStation.subclass = EVChargingStationSub
# end class EVChargingStationSub


class PowerPlantSub(supermod.PowerPlant):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, fuel=None, maxLoad=None, minLoad=None, effMaxLoad=None, effMinLoad=None, energyCarrier=None, mustRun=None):
        super(PowerPlantSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, fuel, maxLoad, minLoad, effMaxLoad, effMinLoad, energyCarrier, mustRun, )
supermod.PowerPlant.subclass = PowerPlantSub
# end class PowerPlantSub


class GConnectionSub(supermod.GConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(GConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.GConnection.subclass = GConnectionSub
# end class GConnectionSub


class HConnectionSub(supermod.HConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(HConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.HConnection.subclass = HConnectionSub
# end class HConnectionSub


class EConnectionSub(supermod.EConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, EANCode=None):
        super(EConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, EANCode, )
supermod.EConnection.subclass = EConnectionSub
# end class EConnectionSub


class HeatExchangeSub(supermod.HeatExchange):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(HeatExchangeSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.HeatExchange.subclass = HeatExchangeSub
# end class HeatExchangeSub


class TransformerSub(supermod.Transformer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, voltagePrimary=None, voltageSecundary=None):
        super(TransformerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, voltagePrimary, voltageSecundary, )
supermod.Transformer.subclass = TransformerSub
# end class TransformerSub


class GasDemandSub(supermod.GasDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(GasDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.GasDemand.subclass = GasDemandSub
# end class GasDemandSub


class ElectricityDemandSub(supermod.ElectricityDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(ElectricityDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.ElectricityDemand.subclass = ElectricityDemandSub
# end class ElectricityDemandSub


class HeatingDemandSub(supermod.HeatingDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', type_=None):
        super(HeatingDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, type_, )
supermod.HeatingDemand.subclass = HeatingDemandSub
# end class HeatingDemandSub


class HeatPumpSub(supermod.HeatPump):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, source=None, stages=1, COP=None, additionalHeatingSourceType=None):
        super(HeatPumpSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, source, stages, COP, additionalHeatingSourceType, )
supermod.HeatPump.subclass = HeatPumpSub
# end class HeatPumpSub


class CoGenerationSub(supermod.CoGeneration):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None, extensiontype_=None):
        super(CoGenerationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier, extensiontype_, )
supermod.CoGeneration.subclass = CoGenerationSub
# end class CoGenerationSub


class GeothermalSourceSub(supermod.GeothermalSource):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, wellDepth=None, geothermalSourceType=None, COP=None, aquiferTemperature=None, flowRate=None, outputPower=0.0, pumpPower=None):
        super(GeothermalSourceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, wellDepth, geothermalSourceType, COP, aquiferTemperature, flowRate, outputPower, pumpPower, )
supermod.GeothermalSource.subclass = GeothermalSourceSub
# end class GeothermalSourceSub


class PipeSub(supermod.Pipe):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, diameter=None, length=None):
        super(PipeSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, diameter, length, )
supermod.Pipe.subclass = PipeSub
# end class PipeSub


class SinkConsumerSub(supermod.SinkConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(SinkConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.SinkConsumer.subclass = SinkConsumerSub
# end class SinkConsumerSub


class SourceProducerSub(supermod.SourceProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None):
        super(SourceProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, )
supermod.SourceProducer.subclass = SourceProducerSub
# end class SourceProducerSub


class GasNetworkSub(supermod.GasNetwork):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, pressure=None):
        super(GasNetworkSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, pressure, )
supermod.GasNetwork.subclass = GasNetworkSub
# end class GasNetworkSub


class HeatNetworkSub(supermod.HeatNetwork):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, temperature=None, temperatureMin=None, temperatureMax=None):
        super(HeatNetworkSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, temperature, temperatureMin, temperatureMax, )
supermod.HeatNetwork.subclass = HeatNetworkSub
# end class HeatNetworkSub


class GasHeaterSub(supermod.GasHeater):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, minimumBurnRate=0.0, type_=None):
        super(GasHeaterSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, minimumBurnRate, type_, )
supermod.GasHeater.subclass = GasHeaterSub
# end class GasHeaterSub


class HeatStorageSub(supermod.HeatStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None, heatLoss=0.0, minStorageTemperature=None, maxStorageTemperature=None):
        super(HeatStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, heatLoss, minStorageTemperature, maxStorageTemperature, )
supermod.HeatStorage.subclass = HeatStorageSub
# end class HeatStorageSub


class AggregatedStorageSub(supermod.AggregatedStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None, aggregationOf=None):
        super(AggregatedStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, aggregationOf, )
supermod.AggregatedStorage.subclass = AggregatedStorageSub
# end class AggregatedStorageSub


class AggregatedConversionSub(supermod.AggregatedConversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, aggregationOf=None):
        super(AggregatedConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, aggregationOf, )
supermod.AggregatedConversion.subclass = AggregatedConversionSub
# end class AggregatedConversionSub


class AggregatedTransportSub(supermod.AggregatedTransport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, aggregationOf=None):
        super(AggregatedTransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, aggregationOf, )
supermod.AggregatedTransport.subclass = AggregatedTransportSub
# end class AggregatedTransportSub


class GenericConversionSub(supermod.GenericConversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None):
        super(GenericConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, )
supermod.GenericConversion.subclass = GenericConversionSub
# end class GenericConversionSub


class GenericTransportSub(supermod.GenericTransport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None):
        super(GenericTransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, )
supermod.GenericTransport.subclass = GenericTransportSub
# end class GenericTransportSub


class GenericStorageSub(supermod.GenericStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None):
        super(GenericStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, )
supermod.GenericStorage.subclass = GenericStorageSub
# end class GenericStorageSub


class GenericProducerSub(supermod.GenericProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None):
        super(GenericProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, )
supermod.GenericProducer.subclass = GenericProducerSub
# end class GenericProducerSub


class GenericConsumerSub(supermod.GenericConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY'):
        super(GenericConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, )
supermod.GenericConsumer.subclass = GenericConsumerSub
# end class GenericConsumerSub


class AggregatedProducerSub(supermod.AggregatedProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, aggregationOf=None):
        super(AggregatedProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, aggregationOf, )
supermod.AggregatedProducer.subclass = AggregatedProducerSub
# end class AggregatedProducerSub


class AggregatedConsumerSub(supermod.AggregatedConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', aggregationOf=None):
        super(AggregatedConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, aggregationOf, )
supermod.AggregatedConsumer.subclass = AggregatedConsumerSub
# end class AggregatedConsumerSub


class ElectricityCableSub(supermod.ElectricityCable):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, length=None):
        super(ElectricityCableSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, length, )
supermod.ElectricityCable.subclass = ElectricityCableSub
# end class ElectricityCableSub


class ElectricityNetworkSub(supermod.ElectricityNetwork):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, voltage=None):
        super(ElectricityNetworkSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, voltage, )
supermod.ElectricityNetwork.subclass = ElectricityNetworkSub
# end class ElectricityNetworkSub


class BatterySub(supermod.Battery):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, efficiency=None, profile=None, selfDischarge=None, maxChargeDischargeCycli=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, maxChargeRate=None, maxDischargeRate=None):
        super(BatterySub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, efficiency, profile, selfDischarge, maxChargeDischargeCycli, chargeEfficiency, dischargeEfficiency, maxChargeRate, maxDischargeRate, )
supermod.Battery.subclass = BatterySub
# end class BatterySub


class PVPanelSub(supermod.PVPanel):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, panelEfficiency=None, inverterEfficiency=None, angle=None, orientation=None):
        super(PVPanelSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, panelEfficiency, inverterEfficiency, angle, orientation, )
supermod.PVPanel.subclass = PVPanelSub
# end class PVPanelSub


class WindTurbineSub(supermod.WindTurbine):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, rotorDiameter=None, height=None):
        super(WindTurbineSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, rotorDiameter, height, )
supermod.WindTurbine.subclass = WindTurbineSub
# end class WindTurbineSub


class ElectrolyzerSub(supermod.Electrolyzer):
    def __init__(self):
        super(ElectrolyzerSub, self).__init__()
supermod.Electrolyzer.subclass = ElectrolyzerSub
# end class ElectrolyzerSub


class CHPSub(supermod.CHP):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None, CHPType=None):
        super(CHPSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier, CHPType, )
supermod.CHP.subclass = CHPSub
# end class CHPSub


class PVParcSub(supermod.PVParc):
    def __init__(self, numberOfPanels=None):
        super(PVParcSub, self).__init__(numberOfPanels, )
supermod.PVParc.subclass = PVParcSub
# end class PVParcSub


class WindParcSub(supermod.WindParc):
    def __init__(self, numberOfTurbines=None):
        super(WindParcSub, self).__init__(numberOfTurbines, )
supermod.WindParc.subclass = WindParcSub
# end class WindParcSub


class FuelCellSub(supermod.FuelCell):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None):
        super(FuelCellSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier, )
supermod.FuelCell.subclass = FuelCellSub
# end class FuelCellSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EnergySystem'
        rootClass = supermod.EnergySystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:esdl="http://www.tno.nl/esdl/180901"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EnergySystem'
        rootClass = supermod.EnergySystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EnergySystem'
        rootClass = supermod.EnergySystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:esdl="http://www.tno.nl/esdl/180901"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'EnergySystem'
        rootClass = supermod.EnergySystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
