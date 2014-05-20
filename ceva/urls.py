from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('programa.views',
    url(r'^adicionar/$', 'cervejaAdicionar'),
    #url(r'^editar/(?P<pk>\d+)/$', 'cervejaEditar'),
    #url(r'^salvar/$', 'cervejaSalvar'),
    #url(r'^pesquisar/$', 'cervejaPesquisar'),
    #url(r'^excluir/(?P<pk>\d+)/$', 'cerveja.adicionar'),
    url(r'^$', 'index'),

    #url(r'^admin/', include(admin.site.urls)),
)
