import elasticsearch_dsl as es

from eapi import abstract_index
from eapi.models import Post


class Article(abstract_index.DocumentBase):

    title = es.Text(analyzer='snowball', fields={'raw': es.Keyword()})
    body = es.Text(analyzer='snowball')
    tags = es.Keyword()
    published_from = es.Date()

    class Index:
        name = 'blog'
        settings = {
            "number_of_shards": 2,
        }

    def get_model(self):
        return Post

    def get_index_queryset(self):
        # method overriden from ABC
        return self.get_model().objects.filter(
            state='PUBLISHED'
        )

    def get_updated_field(self):
        return 'published_from'

    def prepare_tags(self):
        # I know I could have used Nested()
        # but I need to show this method.
        values = self.obj.tags.all().values_list('name', flat=True)
        return ", ".join(values)

    def create_document_dict(self, obj):
        # this method is required.
        self.obj = obj

        doc = Article(
            title=obj.title,
            body=obj.body,
            tags=self.prepare_tags(),
            published_from=obj.published_from,
        )
        doc.meta.id = obj.id
        return doc.to_dict(include_meta=True)