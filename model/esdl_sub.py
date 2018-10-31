#!/usr/bin/env python

#
# Generated Wed Oct 31 13:00:49 2018 by generateDS.py version 2.30.1.
# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'esdl_sup.py')
#   ('-s', 'esdl_sub.py')
#   ('--root-element', 'EnergySystem')
#   ('--export', 'write etree')
#
# Command line arguments:
#   esdlXML.xsd
#
# Command line:
#   C:\Users\matthijssenef\AppData\Local\Programs\Python\Python37\Scripts\generateDS.py -o "esdl_sup.py" -s "esdl_sub.py" --root-element="EnergySystem" --export="write etree" esdlXML.xsd
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
    def __init__(self, name=None, description=None, geographicalScope=None, id=None, sector=None, measures=None, instance=None, potentials=None, energySystemInformation=None, parties=None, services=None, **kwargs_):
        super(EnergySystemSub, self).__init__(name, description, geographicalScope, id, sector, measures, instance, potentials, energySystemInformation, parties, services,  **kwargs_)
supermod.EnergySystem.subclass = EnergySystemSub
# end class EnergySystemSub


class AreaSub(supermod.Area):
    def __init__(self, id=None, name=None, scope='UNDEFINED', type_=None, geometryReference=None, buildingDensity=None, containingArea=None, isOwnedBy=None, potential=None, location=None, contour=None, socialProperties=None, economicProperties=None, asset=None, area=None, mobilityProperties=None, KPIs=None, **kwargs_):
        super(AreaSub, self).__init__(id, name, scope, type_, geometryReference, buildingDensity, containingArea, isOwnedBy, potential, location, contour, socialProperties, economicProperties, asset, area, mobilityProperties, KPIs,  **kwargs_)
supermod.Area.subclass = AreaSub
# end class AreaSub


class PortSub(supermod.Port):
    def __init__(self, id=None, maxPower=None, simultaneousPower=None, energyasset=None, carrier=None, profile=None, extensiontype_=None, **kwargs_):
        super(PortSub, self).__init__(id, maxPower, simultaneousPower, energyasset, carrier, profile, extensiontype_,  **kwargs_)
supermod.Port.subclass = PortSub
# end class PortSub


class InPortSub(supermod.InPort):
    def __init__(self, id=None, maxPower=None, simultaneousPower=None, energyasset=None, carrier=None, profile=None, connectedTo=None, **kwargs_):
        super(InPortSub, self).__init__(id, maxPower, simultaneousPower, energyasset, carrier, profile, connectedTo,  **kwargs_)
supermod.InPort.subclass = InPortSub
# end class InPortSub


class OutPortSub(supermod.OutPort):
    def __init__(self, id=None, maxPower=None, simultaneousPower=None, energyasset=None, carrier=None, profile=None, connectedTo=None, **kwargs_):
        super(OutPortSub, self).__init__(id, maxPower, simultaneousPower, energyasset, carrier, profile, connectedTo,  **kwargs_)
supermod.OutPort.subclass = OutPortSub
# end class OutPortSub


class EconomicPropertiesSub(supermod.EconomicProperties):
    def __init__(self, averageIncome=None, averageWOZvalue=None, percentageOwnerOccupiedProperties=None, percentageHousingAssociation=None, percentagePrivateRental=None, **kwargs_):
        super(EconomicPropertiesSub, self).__init__(averageIncome, averageWOZvalue, percentageOwnerOccupiedProperties, percentageHousingAssociation, percentagePrivateRental,  **kwargs_)
supermod.EconomicProperties.subclass = EconomicPropertiesSub
# end class EconomicPropertiesSub


class SocialPropertiesSub(supermod.SocialProperties):
    def __init__(self, socialCohesion=None, populationDensity=None, numberOfInhabitants=None, **kwargs_):
        super(SocialPropertiesSub, self).__init__(socialCohesion, populationDensity, numberOfInhabitants,  **kwargs_)
supermod.SocialProperties.subclass = SocialPropertiesSub
# end class SocialPropertiesSub


class ItemSub(supermod.Item):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, extensiontype_=None, **kwargs_):
        super(ItemSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, extensiontype_,  **kwargs_)
supermod.Item.subclass = ItemSub
# end class ItemSub


class MeasuresSub(supermod.Measures):
    def __init__(self, asset=None, measuresCollection=None, **kwargs_):
        super(MeasuresSub, self).__init__(asset, measuresCollection,  **kwargs_)
supermod.Measures.subclass = MeasuresSub
# end class MeasuresSub


class InstanceSub(supermod.Instance):
    def __init__(self, id=None, name=None, description=None, detailLevel='UNDEFINED', aggrType=None, area=None, date=None, **kwargs_):
        super(InstanceSub, self).__init__(id, name, description, detailLevel, aggrType, area, date,  **kwargs_)
supermod.Instance.subclass = InstanceSub
# end class InstanceSub


class ServiceSub(supermod.Service):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, extensiontype_=None, **kwargs_):
        super(ServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, extensiontype_,  **kwargs_)
supermod.Service.subclass = ServiceSub
# end class ServiceSub


class PotentialSub(supermod.Potential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, extensiontype_=None, **kwargs_):
        super(PotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, extensiontype_,  **kwargs_)
supermod.Potential.subclass = PotentialSub
# end class PotentialSub


class PotentialsSub(supermod.Potentials):
    def __init__(self, potentials=None, **kwargs_):
        super(PotentialsSub, self).__init__(potentials,  **kwargs_)
supermod.Potentials.subclass = PotentialsSub
# end class PotentialsSub


class CarriersSub(supermod.Carriers):
    def __init__(self, carrier=None, dataSource=None, **kwargs_):
        super(CarriersSub, self).__init__(carrier, dataSource,  **kwargs_)
supermod.Carriers.subclass = CarriersSub
# end class CarriersSub


class EnergySystemInformationSub(supermod.EnergySystemInformation):
    def __init__(self, carriers=None, profiles=None, dataSources=None, mobilityFuelInformation=None, quantityAndUnits=None, sectors=None, **kwargs_):
        super(EnergySystemInformationSub, self).__init__(carriers, profiles, dataSources, mobilityFuelInformation, quantityAndUnits, sectors,  **kwargs_)
supermod.EnergySystemInformation.subclass = EnergySystemInformationSub
# end class EnergySystemInformationSub


class GenericProfileSub(supermod.GenericProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, extensiontype_=None, **kwargs_):
        super(GenericProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, extensiontype_,  **kwargs_)
supermod.GenericProfile.subclass = GenericProfileSub
# end class GenericProfileSub


class StaticProfileSub(supermod.StaticProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, extensiontype_=None, **kwargs_):
        super(StaticProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, extensiontype_,  **kwargs_)
supermod.StaticProfile.subclass = StaticProfileSub
# end class StaticProfileSub


class DateTimeProfileSub(supermod.DateTimeProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, element=None, **kwargs_):
        super(DateTimeProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, element,  **kwargs_)
supermod.DateTimeProfile.subclass = DateTimeProfileSub
# end class DateTimeProfileSub


class ProfileElementSub(supermod.ProfileElement):
    def __init__(self, from_=None, to=None, value=None, **kwargs_):
        super(ProfileElementSub, self).__init__(from_, to, value,  **kwargs_)
supermod.ProfileElement.subclass = ProfileElementSub
# end class ProfileElementSub


class ExternalProfileSub(supermod.ExternalProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, extensiontype_=None, **kwargs_):
        super(ExternalProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, extensiontype_,  **kwargs_)
supermod.ExternalProfile.subclass = ExternalProfileSub
# end class ExternalProfileSub


class SingleValueSub(supermod.SingleValue):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, value=None, **kwargs_):
        super(SingleValueSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, value,  **kwargs_)
supermod.SingleValue.subclass = SingleValueSub
# end class SingleValueSub


class GenericDistributionSub(supermod.GenericDistribution):
    def __init__(self, name=None, extensiontype_=None, **kwargs_):
        super(GenericDistributionSub, self).__init__(name, extensiontype_,  **kwargs_)
supermod.GenericDistribution.subclass = GenericDistributionSub
# end class GenericDistributionSub


class PercentileSub(supermod.Percentile):
    def __init__(self, percentile=None, value=None, **kwargs_):
        super(PercentileSub, self).__init__(percentile, value,  **kwargs_)
supermod.Percentile.subclass = PercentileSub
# end class PercentileSub


class PercentileDistributionSub(supermod.PercentileDistribution):
    def __init__(self, name=None, percentile=None, **kwargs_):
        super(PercentileDistributionSub, self).__init__(name, percentile,  **kwargs_)
supermod.PercentileDistribution.subclass = PercentileDistributionSub
# end class PercentileDistributionSub


class CostInformationSub(supermod.CostInformation):
    def __init__(self, investmentCosts=None, installationCosts=None, O_and_MCosts=None, **kwargs_):
        super(CostInformationSub, self).__init__(investmentCosts, installationCosts, O_and_MCosts,  **kwargs_)
supermod.CostInformation.subclass = CostInformationSub
# end class CostInformationSub


class LabelDistributionSub(supermod.LabelDistribution):
    def __init__(self, name=None, extensiontype_=None, **kwargs_):
        super(LabelDistributionSub, self).__init__(name, extensiontype_,  **kwargs_)
supermod.LabelDistribution.subclass = LabelDistributionSub
# end class LabelDistributionSub


class StringLabelDistributionSub(supermod.StringLabelDistribution):
    def __init__(self, name=None, stringPerc=None, **kwargs_):
        super(StringLabelDistributionSub, self).__init__(name, stringPerc,  **kwargs_)
supermod.StringLabelDistribution.subclass = StringLabelDistributionSub
# end class StringLabelDistributionSub


class EnergyLabelDistributionSub(supermod.EnergyLabelDistribution):
    def __init__(self, name=None, labelPerc=None, **kwargs_):
        super(EnergyLabelDistributionSub, self).__init__(name, labelPerc,  **kwargs_)
supermod.EnergyLabelDistribution.subclass = EnergyLabelDistributionSub
# end class EnergyLabelDistributionSub


class StringPercSub(supermod.StringPerc):
    def __init__(self, label=None, percentage=None, **kwargs_):
        super(StringPercSub, self).__init__(label, percentage,  **kwargs_)
supermod.StringPerc.subclass = StringPercSub
# end class StringPercSub


class EnergyLabelPercSub(supermod.EnergyLabelPerc):
    def __init__(self, energyLabel=None, percentage=None, **kwargs_):
        super(EnergyLabelPercSub, self).__init__(energyLabel, percentage,  **kwargs_)
supermod.EnergyLabelPerc.subclass = EnergyLabelPercSub
# end class EnergyLabelPercSub


class FromToDistributionSub(supermod.FromToDistribution):
    def __init__(self, name=None, fromToPerc=None, **kwargs_):
        super(FromToDistributionSub, self).__init__(name, fromToPerc,  **kwargs_)
supermod.FromToDistribution.subclass = FromToDistributionSub
# end class FromToDistributionSub


class FromToPercSub(supermod.FromToPerc):
    def __init__(self, from_=None, to=None, percentage=None, **kwargs_):
        super(FromToPercSub, self).__init__(from_, to, percentage,  **kwargs_)
supermod.FromToPerc.subclass = FromToPercSub
# end class FromToPercSub


class PItemStatSub(supermod.PItemStat):
    def __init__(self, value=None, sigma=None, **kwargs_):
        super(PItemStatSub, self).__init__(value, sigma,  **kwargs_)
supermod.PItemStat.subclass = PItemStatSub
# end class PItemStatSub


class AbstractVarianceSub(supermod.AbstractVariance):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(AbstractVarianceSub, self).__init__(extensiontype_,  **kwargs_)
supermod.AbstractVariance.subclass = AbstractVarianceSub
# end class AbstractVarianceSub


class SymetricVarianceSub(supermod.SymetricVariance):
    def __init__(self, sigma=None, **kwargs_):
        super(SymetricVarianceSub, self).__init__(sigma,  **kwargs_)
supermod.SymetricVariance.subclass = SymetricVarianceSub
# end class SymetricVarianceSub


class AssymetricVarianceSub(supermod.AssymetricVariance):
    def __init__(self, sigmaMin=None, sigmaPlus=None, **kwargs_):
        super(AssymetricVarianceSub, self).__init__(sigmaMin, sigmaPlus,  **kwargs_)
supermod.AssymetricVariance.subclass = AssymetricVarianceSub
# end class AssymetricVarianceSub


class DoubleAssymetricVarianceSub(supermod.DoubleAssymetricVariance):
    def __init__(self, plus34perc=None, plus48perc=None, min34perc=None, min48perc=None, **kwargs_):
        super(DoubleAssymetricVarianceSub, self).__init__(plus34perc, plus48perc, min34perc, min48perc,  **kwargs_)
supermod.DoubleAssymetricVariance.subclass = DoubleAssymetricVarianceSub
# end class DoubleAssymetricVarianceSub


class PartySub(supermod.Party):
    def __init__(self, id=None, name=None, shortName=None, owns=None, ownsArea=None, sector=None, **kwargs_):
        super(PartySub, self).__init__(id, name, shortName, owns, ownsArea, sector,  **kwargs_)
supermod.Party.subclass = PartySub
# end class PartySub


class URIProfileSub(supermod.URIProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, URI=None, **kwargs_):
        super(URIProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, URI,  **kwargs_)
supermod.URIProfile.subclass = URIProfileSub
# end class URIProfileSub


class DatabaseProfileSub(supermod.DatabaseProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, host=None, port=None, database=None, filters=None, extensiontype_=None, **kwargs_):
        super(DatabaseProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, host, port, database, filters, extensiontype_,  **kwargs_)
supermod.DatabaseProfile.subclass = DatabaseProfileSub
# end class DatabaseProfileSub


class InfluxDBProfileSub(supermod.InfluxDBProfile):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1.0, host=None, port=None, database=None, filters=None, measurement=None, field=None, **kwargs_):
        super(InfluxDBProfileSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, host, port, database, filters, measurement, field,  **kwargs_)
supermod.InfluxDBProfile.subclass = InfluxDBProfileSub
# end class InfluxDBProfileSub


class GeometrySub(supermod.Geometry):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(GeometrySub, self).__init__(extensiontype_,  **kwargs_)
supermod.Geometry.subclass = GeometrySub
# end class GeometrySub


class CarrierSub(supermod.Carrier):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, extensiontype_=None, **kwargs_):
        super(CarrierSub, self).__init__(name, id, cost, dataSource, extensiontype_,  **kwargs_)
supermod.Carrier.subclass = CarrierSub
# end class CarrierSub


class RangeSub(supermod.Range):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, minValue=None, maxValue=None, **kwargs_):
        super(RangeSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, minValue, maxValue,  **kwargs_)
supermod.Range.subclass = RangeSub
# end class RangeSub


class DurationSub(supermod.Duration):
    def __init__(self, value=None, durationUnit='SECOND', **kwargs_):
        super(DurationSub, self).__init__(value, durationUnit,  **kwargs_)
supermod.Duration.subclass = DurationSub
# end class DurationSub


class ProfileReferenceSub(supermod.ProfileReference):
    def __init__(self, name=None, profileType='UNDEFINED', id=None, dataSource=None, profileQuantityAndUnit=None, multiplier=1, reference=None, **kwargs_):
        super(ProfileReferenceSub, self).__init__(name, profileType, id, dataSource, profileQuantityAndUnit, multiplier, reference,  **kwargs_)
supermod.ProfileReference.subclass = ProfileReferenceSub
# end class ProfileReferenceSub


class ProfilesSub(supermod.Profiles):
    def __init__(self, profile=None, **kwargs_):
        super(ProfilesSub, self).__init__(profile,  **kwargs_)
supermod.Profiles.subclass = ProfilesSub
# end class ProfilesSub


class PartiesSub(supermod.Parties):
    def __init__(self, party=None, **kwargs_):
        super(PartiesSub, self).__init__(party,  **kwargs_)
supermod.Parties.subclass = PartiesSub
# end class PartiesSub


class DataSourcesSub(supermod.DataSources):
    def __init__(self, dataSource=None, **kwargs_):
        super(DataSourcesSub, self).__init__(dataSource,  **kwargs_)
supermod.DataSources.subclass = DataSourcesSub
# end class DataSourcesSub


class SubPolygonSub(supermod.SubPolygon):
    def __init__(self, point=None, **kwargs_):
        super(SubPolygonSub, self).__init__(point,  **kwargs_)
supermod.SubPolygon.subclass = SubPolygonSub
# end class SubPolygonSub


class MultiPolygonSub(supermod.MultiPolygon):
    def __init__(self, polygon=None, **kwargs_):
        super(MultiPolygonSub, self).__init__(polygon,  **kwargs_)
supermod.MultiPolygon.subclass = MultiPolygonSub
# end class MultiPolygonSub


class MobilityFuelInformationSub(supermod.MobilityFuelInformation):
    def __init__(self, vehicleFuelEfficiency=None, dataSource=None, **kwargs_):
        super(MobilityFuelInformationSub, self).__init__(vehicleFuelEfficiency, dataSource,  **kwargs_)
supermod.MobilityFuelInformation.subclass = MobilityFuelInformationSub
# end class MobilityFuelInformationSub


class VehicleFuelEfficiencySub(supermod.VehicleFuelEfficiency):
    def __init__(self, vehicleType=None, fuel=None, efficiency=None, **kwargs_):
        super(VehicleFuelEfficiencySub, self).__init__(vehicleType, fuel, efficiency,  **kwargs_)
supermod.VehicleFuelEfficiency.subclass = VehicleFuelEfficiencySub
# end class VehicleFuelEfficiencySub


class MobilityPropertiesSub(supermod.MobilityProperties):
    def __init__(self, numberOfVehicles=None, **kwargs_):
        super(MobilityPropertiesSub, self).__init__(numberOfVehicles,  **kwargs_)
supermod.MobilityProperties.subclass = MobilityPropertiesSub
# end class MobilityPropertiesSub


class NumberOfVehiclesSub(supermod.NumberOfVehicles):
    def __init__(self, vehicleCount=None, **kwargs_):
        super(NumberOfVehiclesSub, self).__init__(vehicleCount,  **kwargs_)
supermod.NumberOfVehicles.subclass = NumberOfVehiclesSub
# end class NumberOfVehiclesSub


class VehicleCountSub(supermod.VehicleCount):
    def __init__(self, type_=None, count=None, **kwargs_):
        super(VehicleCountSub, self).__init__(type_, count,  **kwargs_)
supermod.VehicleCount.subclass = VehicleCountSub
# end class VehicleCountSub


class ServicesSub(supermod.Services):
    def __init__(self, service=None, **kwargs_):
        super(ServicesSub, self).__init__(service,  **kwargs_)
supermod.Services.subclass = ServicesSub
# end class ServicesSub


class AbstractDataSourceSub(supermod.AbstractDataSource):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(AbstractDataSourceSub, self).__init__(extensiontype_,  **kwargs_)
supermod.AbstractDataSource.subclass = AbstractDataSourceSub
# end class AbstractDataSourceSub


class DataSourceReferenceSub(supermod.DataSourceReference):
    def __init__(self, reference=None, **kwargs_):
        super(DataSourceReferenceSub, self).__init__(reference,  **kwargs_)
supermod.DataSourceReference.subclass = DataSourceReferenceSub
# end class DataSourceReferenceSub


class KPIsSub(supermod.KPIs):
    def __init__(self, description=None, kpi=None, **kwargs_):
        super(KPIsSub, self).__init__(description, kpi,  **kwargs_)
supermod.KPIs.subclass = KPIsSub
# end class KPIsSub


class KPISub(supermod.KPI):
    def __init__(self, name=None, value=None, quantityAndUnit=None, **kwargs_):
        super(KPISub, self).__init__(name, value, quantityAndUnit,  **kwargs_)
supermod.KPI.subclass = KPISub
# end class KPISub


class QuantityAndUnitsSub(supermod.QuantityAndUnits):
    def __init__(self, quantityAndUnit=None, **kwargs_):
        super(QuantityAndUnitsSub, self).__init__(quantityAndUnit,  **kwargs_)
supermod.QuantityAndUnits.subclass = QuantityAndUnitsSub
# end class QuantityAndUnitsSub


class AbstractQuantityAndUnitSub(supermod.AbstractQuantityAndUnit):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(AbstractQuantityAndUnitSub, self).__init__(extensiontype_,  **kwargs_)
supermod.AbstractQuantityAndUnit.subclass = AbstractQuantityAndUnitSub
# end class AbstractQuantityAndUnitSub


class QuantityAndUnitReferenceSub(supermod.QuantityAndUnitReference):
    def __init__(self, reference=None, **kwargs_):
        super(QuantityAndUnitReferenceSub, self).__init__(reference,  **kwargs_)
supermod.QuantityAndUnitReference.subclass = QuantityAndUnitReferenceSub
# end class QuantityAndUnitReferenceSub


class ParametersSub(supermod.Parameters):
    def __init__(self, name=None, parameterUnit=None, extensiontype_=None, **kwargs_):
        super(ParametersSub, self).__init__(name, parameterUnit, extensiontype_,  **kwargs_)
supermod.Parameters.subclass = ParametersSub
# end class ParametersSub


class StringParameterSub(supermod.StringParameter):
    def __init__(self, name=None, parameterUnit=None, value=None, **kwargs_):
        super(StringParameterSub, self).__init__(name, parameterUnit, value,  **kwargs_)
supermod.StringParameter.subclass = StringParameterSub
# end class StringParameterSub


class DoubleParameterSub(supermod.DoubleParameter):
    def __init__(self, name=None, parameterUnit=None, value=None, **kwargs_):
        super(DoubleParameterSub, self).__init__(name, parameterUnit, value,  **kwargs_)
supermod.DoubleParameter.subclass = DoubleParameterSub
# end class DoubleParameterSub


class IntegerParameterSub(supermod.IntegerParameter):
    def __init__(self, name=None, parameterUnit=None, value=None, **kwargs_):
        super(IntegerParameterSub, self).__init__(name, parameterUnit, value,  **kwargs_)
supermod.IntegerParameter.subclass = IntegerParameterSub
# end class IntegerParameterSub


class BooleanParameterSub(supermod.BooleanParameter):
    def __init__(self, name=None, parameterUnit=None, value=None, **kwargs_):
        super(BooleanParameterSub, self).__init__(name, parameterUnit, value,  **kwargs_)
supermod.BooleanParameter.subclass = BooleanParameterSub
# end class BooleanParameterSub


class MeasuresCollectionSub(supermod.MeasuresCollection):
    def __init__(self, id=None, name=None, description=None, asset=None, costInformation=None, dataSource=None, **kwargs_):
        super(MeasuresCollectionSub, self).__init__(id, name, description, asset, costInformation, dataSource,  **kwargs_)
supermod.MeasuresCollection.subclass = MeasuresCollectionSub
# end class MeasuresCollectionSub


class PotentialsTypeSub(supermod.PotentialsType):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, extensiontype_=None, **kwargs_):
        super(PotentialsTypeSub, self).__init__(id, name, description, dataSource, quantityAndUnit, extensiontype_,  **kwargs_)
supermod.PotentialsType.subclass = PotentialsTypeSub
# end class PotentialsTypeSub


class SolarFieldPotentialsSub(supermod.SolarFieldPotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(SolarFieldPotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.SolarFieldPotentials.subclass = SolarFieldPotentialsSub
# end class SolarFieldPotentialsSub


class WindPotentialsSub(supermod.WindPotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(WindPotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.WindPotentials.subclass = WindPotentialsSub
# end class WindPotentialsSub


class GeothermalPotentialsSub(supermod.GeothermalPotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(GeothermalPotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.GeothermalPotentials.subclass = GeothermalPotentialsSub
# end class GeothermalPotentialsSub


class LegalAreasSub(supermod.LegalAreas):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, legalarea=None, **kwargs_):
        super(LegalAreasSub, self).__init__(id, name, description, dataSource, quantityAndUnit, legalarea,  **kwargs_)
supermod.LegalAreas.subclass = LegalAreasSub
# end class LegalAreasSub


class ResidualHeatSourcePotentialsSub(supermod.ResidualHeatSourcePotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(ResidualHeatSourcePotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.ResidualHeatSourcePotentials.subclass = ResidualHeatSourcePotentialsSub
# end class ResidualHeatSourcePotentialsSub


class AreaPotentialSub(supermod.AreaPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, extensiontype_=None, **kwargs_):
        super(AreaPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, extensiontype_,  **kwargs_)
supermod.AreaPotential.subclass = AreaPotentialSub
# end class AreaPotentialSub


class AssetPotentialSub(supermod.AssetPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, asset=None, extensiontype_=None, **kwargs_):
        super(AssetPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, asset, extensiontype_,  **kwargs_)
supermod.AssetPotential.subclass = AssetPotentialSub
# end class AssetPotentialSub


class SectorsSub(supermod.Sectors):
    def __init__(self, sector=None, dataSource=None, **kwargs_):
        super(SectorsSub, self).__init__(sector, dataSource,  **kwargs_)
supermod.Sectors.subclass = SectorsSub
# end class SectorsSub


class SectorSub(supermod.Sector):
    def __init__(self, id=None, name=None, description=None, code=None, dataSource=None, **kwargs_):
        super(SectorSub, self).__init__(id, name, description, code, dataSource,  **kwargs_)
supermod.Sector.subclass = SectorSub
# end class SectorSub


class MultiLineSub(supermod.MultiLine):
    def __init__(self, line=None, **kwargs_):
        super(MultiLineSub, self).__init__(line,  **kwargs_)
supermod.MultiLine.subclass = MultiLineSub
# end class MultiLineSub


class AbstractGTPotentialSub(supermod.AbstractGTPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, extensiontype_=None, **kwargs_):
        super(AbstractGTPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, extensiontype_,  **kwargs_)
supermod.AbstractGTPotential.subclass = AbstractGTPotentialSub
# end class AbstractGTPotentialSub


class UTESPotentialsSub(supermod.UTESPotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(UTESPotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.UTESPotentials.subclass = UTESPotentialsSub
# end class UTESPotentialsSub


class UTESPotentialSub(supermod.UTESPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, value=None, type_=None, **kwargs_):
        super(UTESPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, value, type_,  **kwargs_)
supermod.UTESPotential.subclass = UTESPotentialSub
# end class UTESPotentialSub


class AbstractInstanceDateSub(supermod.AbstractInstanceDate):
    def __init__(self, extensiontype_=None, **kwargs_):
        super(AbstractInstanceDateSub, self).__init__(extensiontype_,  **kwargs_)
supermod.AbstractInstanceDate.subclass = AbstractInstanceDateSub
# end class AbstractInstanceDateSub


class InstanceDateSub(supermod.InstanceDate):
    def __init__(self, date=None, **kwargs_):
        super(InstanceDateSub, self).__init__(date,  **kwargs_)
supermod.InstanceDate.subclass = InstanceDateSub
# end class InstanceDateSub


class InstancePeriodSub(supermod.InstancePeriod):
    def __init__(self, fromDate=None, toDate=None, **kwargs_):
        super(InstancePeriodSub, self).__init__(fromDate, toDate,  **kwargs_)
supermod.InstancePeriod.subclass = InstancePeriodSub
# end class InstancePeriodSub


class RoomHeaterSub(supermod.RoomHeater):
    def __init__(self, type_=None, **kwargs_):
        super(RoomHeaterSub, self).__init__(type_,  **kwargs_)
supermod.RoomHeater.subclass = RoomHeaterSub
# end class RoomHeaterSub


class BiomassPotentialsSub(supermod.BiomassPotentials):
    def __init__(self, id=None, name=None, description=None, dataSource=None, quantityAndUnit=None, potential=None, **kwargs_):
        super(BiomassPotentialsSub, self).__init__(id, name, description, dataSource, quantityAndUnit, potential,  **kwargs_)
supermod.BiomassPotentials.subclass = BiomassPotentialsSub
# end class BiomassPotentialsSub


class BiomassPotentialSub(supermod.BiomassPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, value=0.0, **kwargs_):
        super(BiomassPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, value,  **kwargs_)
supermod.BiomassPotential.subclass = BiomassPotentialSub
# end class BiomassPotentialSub


class GeothermalEnergyPotentialSub(supermod.GeothermalEnergyPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, depth=None, value=0.0, **kwargs_):
        super(GeothermalEnergyPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, depth, value,  **kwargs_)
supermod.GeothermalEnergyPotential.subclass = GeothermalEnergyPotentialSub
# end class GeothermalEnergyPotentialSub


class QuantityAndUnitTypeSub(supermod.QuantityAndUnitType):
    def __init__(self, physicalQuantity=None, multiplier=None, unit=None, perMultiplier=None, perUnit=None, description=None, perTimeUnit=None, id=None, **kwargs_):
        super(QuantityAndUnitTypeSub, self).__init__(physicalQuantity, multiplier, unit, perMultiplier, perUnit, description, perTimeUnit, id,  **kwargs_)
supermod.QuantityAndUnitType.subclass = QuantityAndUnitTypeSub
# end class QuantityAndUnitTypeSub


class ResidualHeatSourcePotentialSub(supermod.ResidualHeatSourcePotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, asset=None, value=0.0, type_=None, **kwargs_):
        super(ResidualHeatSourcePotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, asset, value, type_,  **kwargs_)
supermod.ResidualHeatSourcePotential.subclass = ResidualHeatSourcePotentialSub
# end class ResidualHeatSourcePotentialSub


class DataSourceSub(supermod.DataSource):
    def __init__(self, id=None, name=None, description=None, reference=None, attribution=None, releaseDate=None, version=None, licence=None, **kwargs_):
        super(DataSourceSub, self).__init__(id, name, description, reference, attribution, releaseDate, version, licence,  **kwargs_)
supermod.DataSource.subclass = DataSourceSub
# end class DataSourceSub


class SolarFieldPotentialSub(supermod.SolarFieldPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, value=0.0, **kwargs_):
        super(SolarFieldPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, value,  **kwargs_)
supermod.SolarFieldPotential.subclass = SolarFieldPotentialSub
# end class SolarFieldPotentialSub


class CommoditySub(supermod.Commodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, extensiontype_=None, **kwargs_):
        super(CommoditySub, self).__init__(name, id, cost, dataSource, extensiontype_,  **kwargs_)
supermod.Commodity.subclass = CommoditySub
# end class CommoditySub


class LineSub(supermod.Line):
    def __init__(self, point=None, **kwargs_):
        super(LineSub, self).__init__(point,  **kwargs_)
supermod.Line.subclass = LineSub
# end class LineSub


class EnergyCarrierSub(supermod.EnergyCarrier):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, energyContent=0.0, emission=0.0, energyCarrierType=None, stateOfMatter=None, energyContentUnit=None, emissionUnit=None, **kwargs_):
        super(EnergyCarrierSub, self).__init__(name, id, cost, dataSource, energyContent, emission, energyCarrierType, stateOfMatter, energyContentUnit, emissionUnit,  **kwargs_)
supermod.EnergyCarrier.subclass = EnergyCarrierSub
# end class EnergyCarrierSub


class WindPotentialSub(supermod.WindPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, value=None, height=None, **kwargs_):
        super(WindPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, value, height,  **kwargs_)
supermod.WindPotential.subclass = WindPotentialSub
# end class WindPotentialSub


class EnergyServiceSub(supermod.EnergyService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, extensiontype_=None, **kwargs_):
        super(EnergyServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, extensiontype_,  **kwargs_)
supermod.EnergyService.subclass = EnergyServiceSub
# end class EnergyServiceSub


class LegalAreaSub(supermod.LegalArea):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, purpose=None, **kwargs_):
        super(LegalAreaSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, purpose,  **kwargs_)
supermod.LegalArea.subclass = LegalAreaSub
# end class LegalAreaSub


class PolygonSub(supermod.Polygon):
    def __init__(self, exterior=None, interior=None, **kwargs_):
        super(PolygonSub, self).__init__(exterior, interior,  **kwargs_)
supermod.Polygon.subclass = PolygonSub
# end class PolygonSub


class PointSub(supermod.Point):
    def __init__(self, lat=None, lon=None, **kwargs_):
        super(PointSub, self).__init__(lat, lon,  **kwargs_)
supermod.Point.subclass = PointSub
# end class PointSub


class GeothermalPotentialSub(supermod.GeothermalPotential):
    def __init__(self, id=None, name=None, geometryReference=None, geometry=None, dataSource=None, quantityAndUnit=None, area=None, temperature=None, depth=None, potential=None, powerPerDoublet='UNKNOWN', **kwargs_):
        super(GeothermalPotentialSub, self).__init__(id, name, geometryReference, geometry, dataSource, quantityAndUnit, area, temperature, depth, potential, powerPerDoublet,  **kwargs_)
supermod.GeothermalPotential.subclass = GeothermalPotentialSub
# end class GeothermalPotentialSub


class AssetSub(supermod.Asset):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, extensiontype_=None, **kwargs_):
        super(AssetSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, extensiontype_,  **kwargs_)
supermod.Asset.subclass = AssetSub
# end class AssetSub


class EnergyAssetSub(supermod.EnergyAsset):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, extensiontype_=None, **kwargs_):
        super(EnergyAssetSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, extensiontype_,  **kwargs_)
supermod.EnergyAsset.subclass = EnergyAssetSub
# end class EnergyAssetSub


class EnergyMarketSub(supermod.EnergyMarket):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, asset=None, carrier=None, parameters=None, **kwargs_):
        super(EnergyMarketSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, asset, carrier, parameters,  **kwargs_)
supermod.EnergyMarket.subclass = EnergyMarketSub
# end class EnergyMarketSub


class ControlStrategySub(supermod.ControlStrategy):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, energyAsset=None, extensiontype_=None, **kwargs_):
        super(ControlStrategySub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, energyAsset, extensiontype_,  **kwargs_)
supermod.ControlStrategy.subclass = ControlStrategySub
# end class ControlStrategySub


class EnergyCommoditySub(supermod.EnergyCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, **kwargs_):
        super(EnergyCommoditySub, self).__init__(name, id, cost, dataSource,  **kwargs_)
supermod.EnergyCommodity.subclass = EnergyCommoditySub
# end class EnergyCommoditySub


class ElectricityCommoditySub(supermod.ElectricityCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, voltage=None, **kwargs_):
        super(ElectricityCommoditySub, self).__init__(name, id, cost, dataSource, voltage,  **kwargs_)
supermod.ElectricityCommodity.subclass = ElectricityCommoditySub
# end class ElectricityCommoditySub


class HeatCommoditySub(supermod.HeatCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, temperature=None, **kwargs_):
        super(HeatCommoditySub, self).__init__(name, id, cost, dataSource, temperature,  **kwargs_)
supermod.HeatCommodity.subclass = HeatCommoditySub
# end class HeatCommoditySub


class GasCommoditySub(supermod.GasCommodity):
    def __init__(self, name=None, id=None, cost=None, dataSource=None, pressure=None, **kwargs_):
        super(GasCommoditySub, self).__init__(name, id, cost, dataSource, pressure,  **kwargs_)
supermod.GasCommodity.subclass = GasCommoditySub
# end class GasCommoditySub


class AggregatorServiceSub(supermod.AggregatorService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, **kwargs_):
        super(AggregatorServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource,  **kwargs_)
supermod.AggregatorService.subclass = AggregatorServiceSub
# end class AggregatorServiceSub


class AbstractBuildingSub(supermod.AbstractBuilding):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, extensiontype_=None, **kwargs_):
        super(AbstractBuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, extensiontype_,  **kwargs_)
supermod.AbstractBuilding.subclass = AbstractBuildingSub
# end class AbstractBuildingSub


class DemandResponseServiceSub(supermod.DemandResponseService):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, **kwargs_):
        super(DemandResponseServiceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource,  **kwargs_)
supermod.DemandResponseService.subclass = DemandResponseServiceSub
# end class DemandResponseServiceSub


class InsulationSub(supermod.Insulation):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, thermalInsulation=None, **kwargs_):
        super(InsulationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, thermalInsulation,  **kwargs_)
supermod.Insulation.subclass = InsulationSub
# end class InsulationSub


class BuildingSub(supermod.Building):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, buildingYear=None, residentialBuildingType=None, floorArea=None, numberOfFloors=None, slantedRoofArea=None, flatRoofArea=None, roofType=None, wallArea=None, windowArea=None, perimeter=None, height=None, rcFloor=None, rcWall=None, rcRoof=None, uWindow=None, orientation=None, glasType=None, ventilationType=None, **kwargs_):
        super(BuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, buildingYear, residentialBuildingType, floorArea, numberOfFloors, slantedRoofArea, flatRoofArea, roofType, wallArea, windowArea, perimeter, height, rcFloor, rcWall, rcRoof, uWindow, orientation, glasType, ventilationType,  **kwargs_)
supermod.Building.subclass = BuildingSub
# end class BuildingSub


class BuildingUnitSub(supermod.BuildingUnit):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, type_=None, housingType=None, numberOfInhabitants=None, inhabitantsType=None, **kwargs_):
        super(BuildingUnitSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, type_, housingType, numberOfInhabitants, inhabitantsType,  **kwargs_)
supermod.BuildingUnit.subclass = BuildingUnitSub
# end class BuildingUnitSub


class TransportSub(supermod.Transport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None, **kwargs_):
        super(TransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_,  **kwargs_)
supermod.Transport.subclass = TransportSub
# end class TransportSub


class ConversionSub(supermod.Conversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, extensiontype_=None, **kwargs_):
        super(ConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, extensiontype_,  **kwargs_)
supermod.Conversion.subclass = ConversionSub
# end class ConversionSub


class StorageSub(supermod.Storage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, extensiontype_=None, **kwargs_):
        super(StorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile, extensiontype_,  **kwargs_)
supermod.Storage.subclass = StorageSub
# end class StorageSub


class ConsumerSub(supermod.Consumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', extensiontype_=None, **kwargs_):
        super(ConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, extensiontype_,  **kwargs_)
supermod.Consumer.subclass = ConsumerSub
# end class ConsumerSub


class ProducerSub(supermod.Producer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, extensiontype_=None, **kwargs_):
        super(ProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, extensiontype_,  **kwargs_)
supermod.Producer.subclass = ProducerSub
# end class ProducerSub


class BiomassHeaterSub(supermod.BiomassHeater):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(BiomassHeaterSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.BiomassHeater.subclass = BiomassHeaterSub
# end class BiomassHeaterSub


class AbstractConnectionSub(supermod.AbstractConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None, **kwargs_):
        super(AbstractConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_,  **kwargs_)
supermod.AbstractConnection.subclass = AbstractConnectionSub
# end class AbstractConnectionSub


class AbstractTransformerSub(supermod.AbstractTransformer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None, **kwargs_):
        super(AbstractTransformerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_,  **kwargs_)
supermod.AbstractTransformer.subclass = AbstractTransformerSub
# end class AbstractTransformerSub


class AbstractSwitchSub(supermod.AbstractSwitch):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None, **kwargs_):
        super(AbstractSwitchSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_,  **kwargs_)
supermod.AbstractSwitch.subclass = AbstractSwitchSub
# end class AbstractSwitchSub


class AbstractConductorSub(supermod.AbstractConductor):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, extensiontype_=None, **kwargs_):
        super(AbstractConductorSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, extensiontype_,  **kwargs_)
supermod.AbstractConductor.subclass = AbstractConductorSub
# end class AbstractConductorSub


class EnergyNetworkSub(supermod.EnergyNetwork):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(EnergyNetworkSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.EnergyNetwork.subclass = EnergyNetworkSub
# end class EnergyNetworkSub


class WaterToPowerSub(supermod.WaterToPower):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, type_=None, **kwargs_):
        super(WaterToPowerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, type_,  **kwargs_)
supermod.WaterToPower.subclass = WaterToPowerSub
# end class WaterToPowerSub


class CircuitBrakerSub(supermod.CircuitBraker):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(CircuitBrakerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.CircuitBraker.subclass = CircuitBrakerSub
# end class CircuitBrakerSub


class DrivenByProfileSub(supermod.DrivenByProfile):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, energyAsset=None, profile=None, **kwargs_):
        super(DrivenByProfileSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, energyAsset, profile,  **kwargs_)
supermod.DrivenByProfile.subclass = DrivenByProfileSub
# end class DrivenByProfileSub


class DrivenBySupplySub(supermod.DrivenBySupply):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, energyAsset=None, inport=None, **kwargs_):
        super(DrivenBySupplySub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, energyAsset, inport,  **kwargs_)
supermod.DrivenBySupply.subclass = DrivenBySupplySub
# end class DrivenBySupplySub


class GasConversionSub(supermod.GasConversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, type_=None, **kwargs_):
        super(GasConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, type_,  **kwargs_)
supermod.GasConversion.subclass = GasConversionSub
# end class GasConversionSub


class DrivenByDemandSub(supermod.DrivenByDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, energyAsset=None, outport=None, **kwargs_):
        super(DrivenByDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, energyAsset, outport,  **kwargs_)
supermod.DrivenByDemand.subclass = DrivenByDemandSub
# end class DrivenByDemandSub


class GasStorageSub(supermod.GasStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, minStoragePressure=None, maxStoragePressure=0.0, **kwargs_):
        super(GasStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile, minStoragePressure, maxStoragePressure,  **kwargs_)
supermod.GasStorage.subclass = GasStorageSub
# end class GasStorageSub


class MobilityDemandSub(supermod.MobilityDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', fuelType=None, distance=None, efficiency=None, type_=None, **kwargs_):
        super(MobilityDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, fuelType, distance, efficiency, type_,  **kwargs_)
supermod.MobilityDemand.subclass = MobilityDemandSub
# end class MobilityDemandSub


class FermentationPlantSub(supermod.FermentationPlant):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(FermentationPlantSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.FermentationPlant.subclass = FermentationPlantSub
# end class FermentationPlantSub


class ResidualHeatSourceSub(supermod.ResidualHeatSource):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, type_=None, **kwargs_):
        super(ResidualHeatSourceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, type_,  **kwargs_)
supermod.ResidualHeatSource.subclass = ResidualHeatSourceSub
# end class ResidualHeatSourceSub


class SolarCollectorSub(supermod.SolarCollector):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, type_=None, **kwargs_):
        super(SolarCollectorSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, type_,  **kwargs_)
supermod.SolarCollector.subclass = SolarCollectorSub
# end class SolarCollectorSub


class EnergyDemandSub(supermod.EnergyDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(EnergyDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.EnergyDemand.subclass = EnergyDemandSub
# end class EnergyDemandSub


class AircoSub(supermod.Airco):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(AircoSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.Airco.subclass = AircoSub
# end class AircoSub


class CoolingDemandSub(supermod.CoolingDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', deviceType=None, **kwargs_):
        super(CoolingDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, deviceType,  **kwargs_)
supermod.CoolingDemand.subclass = CoolingDemandSub
# end class CoolingDemandSub


class ValveSub(supermod.Valve):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(ValveSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.Valve.subclass = ValveSub
# end class ValveSub


class PumpSub(supermod.Pump):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(PumpSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.Pump.subclass = PumpSub
# end class PumpSub


class XToPowerSub(supermod.XToPower):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(XToPowerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.XToPower.subclass = XToPowerSub
# end class XToPowerSub


class CCSSub(supermod.CCS):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, **kwargs_):
        super(CCSSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile,  **kwargs_)
supermod.CCS.subclass = CCSSub
# end class CCSSub


class PowerToXSub(supermod.PowerToX):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(PowerToXSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.PowerToX.subclass = PowerToXSub
# end class PowerToXSub


class LossesSub(supermod.Losses):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(LossesSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.Losses.subclass = LossesSub
# end class LossesSub


class AggregatedBuildingSub(supermod.AggregatedBuilding):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, energyLabel=None, energyIndex=None, asset=None, numberOfBuildings=None, aggregationOf=None, energyLabelDistribution=None, buildingYearDistribution=None, **kwargs_):
        super(AggregatedBuildingSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, energyLabel, energyIndex, asset, numberOfBuildings, aggregationOf, energyLabelDistribution, buildingYearDistribution,  **kwargs_)
supermod.AggregatedBuilding.subclass = AggregatedBuildingSub
# end class AggregatedBuildingSub


class EVChargingStationSub(supermod.EVChargingStation):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(EVChargingStationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.EVChargingStation.subclass = EVChargingStationSub
# end class EVChargingStationSub


class PowerPlantSub(supermod.PowerPlant):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, fuel=None, maxLoad=None, minLoad=None, effMaxLoad=None, effMinLoad=None, energyCarrier=None, mustRun=None, **kwargs_):
        super(PowerPlantSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, fuel, maxLoad, minLoad, effMaxLoad, effMinLoad, energyCarrier, mustRun,  **kwargs_)
supermod.PowerPlant.subclass = PowerPlantSub
# end class PowerPlantSub


class GConnectionSub(supermod.GConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(GConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.GConnection.subclass = GConnectionSub
# end class GConnectionSub


class HConnectionSub(supermod.HConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(HConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.HConnection.subclass = HConnectionSub
# end class HConnectionSub


class EConnectionSub(supermod.EConnection):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, EANCode=None, **kwargs_):
        super(EConnectionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, EANCode,  **kwargs_)
supermod.EConnection.subclass = EConnectionSub
# end class EConnectionSub


class HeatExchangeSub(supermod.HeatExchange):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(HeatExchangeSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.HeatExchange.subclass = HeatExchangeSub
# end class HeatExchangeSub


class TransformerSub(supermod.Transformer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, voltagePrimary=None, voltageSecundary=None, **kwargs_):
        super(TransformerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, voltagePrimary, voltageSecundary,  **kwargs_)
supermod.Transformer.subclass = TransformerSub
# end class TransformerSub


class GasDemandSub(supermod.GasDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(GasDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.GasDemand.subclass = GasDemandSub
# end class GasDemandSub


class ElectricityDemandSub(supermod.ElectricityDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(ElectricityDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.ElectricityDemand.subclass = ElectricityDemandSub
# end class ElectricityDemandSub


class HeatingDemandSub(supermod.HeatingDemand):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', type_=None, deviceType=None, **kwargs_):
        super(HeatingDemandSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, type_, deviceType,  **kwargs_)
supermod.HeatingDemand.subclass = HeatingDemandSub
# end class HeatingDemandSub


class HeatPumpSub(supermod.HeatPump):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, source=None, stages=1, COP=None, additionalHeatingSourceType=None, **kwargs_):
        super(HeatPumpSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, source, stages, COP, additionalHeatingSourceType,  **kwargs_)
supermod.HeatPump.subclass = HeatPumpSub
# end class HeatPumpSub


class CoGenerationSub(supermod.CoGeneration):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None, extensiontype_=None, **kwargs_):
        super(CoGenerationSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier, extensiontype_,  **kwargs_)
supermod.CoGeneration.subclass = CoGenerationSub
# end class CoGenerationSub


class GeothermalSourceSub(supermod.GeothermalSource):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, wellDepth=None, geothermalSourceType=None, COP=None, aquiferTemperature=None, flowRate=None, pumpPower=None, **kwargs_):
        super(GeothermalSourceSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, wellDepth, geothermalSourceType, COP, aquiferTemperature, flowRate, pumpPower,  **kwargs_)
supermod.GeothermalSource.subclass = GeothermalSourceSub
# end class GeothermalSourceSub


class PipeSub(supermod.Pipe):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, diameter=None, length=None, **kwargs_):
        super(PipeSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, diameter, length,  **kwargs_)
supermod.Pipe.subclass = PipeSub
# end class PipeSub


class SinkConsumerSub(supermod.SinkConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(SinkConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.SinkConsumer.subclass = SinkConsumerSub
# end class SinkConsumerSub


class SourceProducerSub(supermod.SourceProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(SourceProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.SourceProducer.subclass = SourceProducerSub
# end class SourceProducerSub


class GasNetworkSub(supermod.GasNetwork):
    def __init__(self, pressure=None, **kwargs_):
        super(GasNetworkSub, self).__init__(pressure,  **kwargs_)
supermod.GasNetwork.subclass = GasNetworkSub
# end class GasNetworkSub


class HeatNetworkSub(supermod.HeatNetwork):
    def __init__(self, temperature=None, temperatureMin=None, temperatureMax=None, **kwargs_):
        super(HeatNetworkSub, self).__init__(temperature, temperatureMin, temperatureMax,  **kwargs_)
supermod.HeatNetwork.subclass = HeatNetworkSub
# end class HeatNetworkSub


class GasHeaterSub(supermod.GasHeater):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, minimumBurnRate=0.0, type_=None, **kwargs_):
        super(GasHeaterSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, minimumBurnRate, type_,  **kwargs_)
supermod.GasHeater.subclass = GasHeaterSub
# end class GasHeaterSub


class HeatStorageSub(supermod.HeatStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, minStorageTemperature=None, maxStorageTemperature=None, **kwargs_):
        super(HeatStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile, minStorageTemperature, maxStorageTemperature,  **kwargs_)
supermod.HeatStorage.subclass = HeatStorageSub
# end class HeatStorageSub


class AggregatedStorageSub(supermod.AggregatedStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, aggregationOf=None, **kwargs_):
        super(AggregatedStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile, aggregationOf,  **kwargs_)
supermod.AggregatedStorage.subclass = AggregatedStorageSub
# end class AggregatedStorageSub


class AggregatedConversionSub(supermod.AggregatedConversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, aggregationOf=None, **kwargs_):
        super(AggregatedConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, aggregationOf,  **kwargs_)
supermod.AggregatedConversion.subclass = AggregatedConversionSub
# end class AggregatedConversionSub


class AggregatedTransportSub(supermod.AggregatedTransport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, aggregationOf=None, **kwargs_):
        super(AggregatedTransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, aggregationOf,  **kwargs_)
supermod.AggregatedTransport.subclass = AggregatedTransportSub
# end class AggregatedTransportSub


class GenericConversionSub(supermod.GenericConversion):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(GenericConversionSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.GenericConversion.subclass = GenericConversionSub
# end class GenericConversionSub


class GenericTransportSub(supermod.GenericTransport):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, **kwargs_):
        super(GenericTransportSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity,  **kwargs_)
supermod.GenericTransport.subclass = GenericTransportSub
# end class GenericTransportSub


class GenericStorageSub(supermod.GenericStorage):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, **kwargs_):
        super(GenericStorageSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile,  **kwargs_)
supermod.GenericStorage.subclass = GenericStorageSub
# end class GenericStorageSub


class GenericProducerSub(supermod.GenericProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, **kwargs_):
        super(GenericProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power,  **kwargs_)
supermod.GenericProducer.subclass = GenericProducerSub
# end class GenericProducerSub


class GenericConsumerSub(supermod.GenericConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', **kwargs_):
        super(GenericConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType,  **kwargs_)
supermod.GenericConsumer.subclass = GenericConsumerSub
# end class GenericConsumerSub


class AggregatedProducerSub(supermod.AggregatedProducer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, aggregationOf=None, **kwargs_):
        super(AggregatedProducerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, aggregationOf,  **kwargs_)
supermod.AggregatedProducer.subclass = AggregatedProducerSub
# end class AggregatedProducerSub


class AggregatedConsumerSub(supermod.AggregatedConsumer):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, consType='PRIMARY', aggregationOf=None, **kwargs_):
        super(AggregatedConsumerSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, consType, aggregationOf,  **kwargs_)
supermod.AggregatedConsumer.subclass = AggregatedConsumerSub
# end class AggregatedConsumerSub


class ElectricityCableSub(supermod.ElectricityCable):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, length=None, **kwargs_):
        super(ElectricityCableSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, length,  **kwargs_)
supermod.ElectricityCable.subclass = ElectricityCableSub
# end class ElectricityCableSub


class ElectricityNetworkSub(supermod.ElectricityNetwork):
    def __init__(self, voltage=None, **kwargs_):
        super(ElectricityNetworkSub, self).__init__(voltage,  **kwargs_)
supermod.ElectricityNetwork.subclass = ElectricityNetworkSub
# end class ElectricityNetworkSub


class BatterySub(supermod.Battery):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, capacity=None, chargeEfficiency=0.0, dischargeEfficiency=0.0, selfDischargeRate=0.0, fillLevel=None, maxChargeRate=0.0, maxDischargeRate=0.0, profile=None, maxChargeDischargeCycles=None, **kwargs_):
        super(BatterySub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, capacity, chargeEfficiency, dischargeEfficiency, selfDischargeRate, fillLevel, maxChargeRate, maxDischargeRate, profile, maxChargeDischargeCycles,  **kwargs_)
supermod.Battery.subclass = BatterySub
# end class BatterySub


class PVPanelSub(supermod.PVPanel):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, panelEfficiency=None, inverterEfficiency=None, angle=None, orientation=None, **kwargs_):
        super(PVPanelSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, panelEfficiency, inverterEfficiency, angle, orientation,  **kwargs_)
supermod.PVPanel.subclass = PVPanelSub
# end class PVPanelSub


class WindTurbineSub(supermod.WindTurbine):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, prodType='RENEWABLE', operationalHours=None, fullLoadHours=None, power=None, rotorDiameter=None, height=None, type_=None, **kwargs_):
        super(WindTurbineSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, prodType, operationalHours, fullLoadHours, power, rotorDiameter, height, type_,  **kwargs_)
supermod.WindTurbine.subclass = WindTurbineSub
# end class WindTurbineSub


class PVInstallationSub(supermod.PVInstallation):
    def __init__(self, type_=None, numberOfPanels=None, **kwargs_):
        super(PVInstallationSub, self).__init__(type_, numberOfPanels,  **kwargs_)
supermod.PVInstallation.subclass = PVInstallationSub
# end class PVInstallationSub


class ElectrolyzerSub(supermod.Electrolyzer):
    def __init__(self, **kwargs_):
        super(ElectrolyzerSub, self).__init__( **kwargs_)
supermod.Electrolyzer.subclass = ElectrolyzerSub
# end class ElectrolyzerSub


class CHPSub(supermod.CHP):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None, CHPType=None, **kwargs_):
        super(CHPSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier, CHPType,  **kwargs_)
supermod.CHP.subclass = CHPSub
# end class CHPSub


class PVParcSub(supermod.PVParc):
    def __init__(self, numberOfPanels=None, **kwargs_):
        super(PVParcSub, self).__init__(numberOfPanels,  **kwargs_)
supermod.PVParc.subclass = PVParcSub
# end class PVParcSub


class WindParcSub(supermod.WindParc):
    def __init__(self, numberOfTurbines=None, **kwargs_):
        super(WindParcSub, self).__init__(numberOfTurbines,  **kwargs_)
supermod.WindParc.subclass = WindParcSub
# end class WindParcSub


class FuelCellSub(supermod.FuelCell):
    def __init__(self, id=None, name=None, shortName=None, description=None, originalIdInSource=None, isOwnedBy=None, sector=None, dataSource=None, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, technicalLifetime=None, area=None, containingBuilding=None, geometry=None, costInformation=None, port=None, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, heatEfficiency=0.0, electricalEfficiency=0.0, HERatio=None, fuelType=None, leadCommodity=None, energyCarrier=None, **kwargs_):
        super(FuelCellSub, self).__init__(id, name, shortName, description, originalIdInSource, isOwnedBy, sector, dataSource, surfaceArea, commissioningDate, decommissioningDate, owner, technicalLifetime, area, containingBuilding, geometry, costInformation, port, efficiency, operationalHours, fullLoadHours, power, heatEfficiency, electricalEfficiency, HERatio, fuelType, leadCommodity, energyCarrier,  **kwargs_)
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
            namespacedef_='xmlns:esdl="http://www.tno.nl/esdl"',
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
            namespacedef_='xmlns:esdl="http://www.tno.nl/esdl"')
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
