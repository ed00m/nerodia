import six

from .element import Element
from ..meta_elements import MetaHTMLElement


@six.add_metaclass(MetaHTMLElement)
class HTMLElement(Element):
    pass

# TODO: collection
@six.add_metaclass(MetaHTMLElement)
class HTMLElementCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Font(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FontCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Directory(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DirectoryCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FrameSet(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FrameSetCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Marquee(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MarqueeCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Applet(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class AppletCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Canvas(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class CanvasCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Template(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TemplateCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Script(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ScriptCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Dialog(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DialogCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MenuItem(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MenuItemCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Menu(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MenuCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Details(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DetailsCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Legend(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class LegendCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FieldSet(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FieldSetCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Meter(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MeterCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Progress(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ProgressCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Output(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OutputCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Keygen(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class KeygenCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TextAreaCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OptionCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OptGroup(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OptGroupCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DataList(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DataListCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class SelectCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ButtonCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class InputCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Label(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class LabelCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class FormCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableCellCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableHeaderCell(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableHeaderCellCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableDataCell(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableDataCellCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableRowCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableSectionCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableCol(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableColCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableCaption(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableCaptionCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TableCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class AreaCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Map(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MapCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Media(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MediaCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Audio(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class AudioCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Video(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class VideoCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Track(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TrackCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Param(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ParamCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Object(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ObjectCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Embed(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class EmbedCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class IFrameCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ImageCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Source(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class SourceCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Picture(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class PictureCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Mod(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ModCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class BR(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class BRCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Span(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class SpanCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Time(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TimeCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Data(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DataCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class AnchorCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Div(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DivCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class DListCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class LI(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class LICollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class UList(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class UListCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OList(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class OListCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Quote(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class QuoteCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Pre(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class PreCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class HR(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class HRCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Paragraph(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class ParagraphCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Heading(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class HeadingCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Body(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class BodyCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Style(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class StyleCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Meta(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class MetaCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Base(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class BaseCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Title(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class TitleCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Head(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class HeadCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Html(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class HtmlCollection(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class Unknown(HTMLElement):
    pass

@six.add_metaclass(MetaHTMLElement)
class UnknownCollection(HTMLElement):
    pass

