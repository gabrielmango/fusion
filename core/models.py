import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_name(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateTimeField('criado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)
    ativo = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'engrenagem'),
        ('lni-starts-up', 'grafico'),
        ('lni-users', 'usuarios'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'foguete'),
    )
    servico = models.CharField('servico', max_length=100)
    descricao = models.CharField('descricao', max_length=200)
    icone = models.CharField('icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=255)
    imagem = StdImageField(
        'Imagem', upload_to=get_file_name, variations={
            'thumb': {
                'width': 480,
                'height': 480,
                'crop': True
            }
        }
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
    
    def __str__(self):
        return self.nome