from django.db import models
from django.core.urlresolvers import reverse_lazy, reverse

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=15, default="Europe")
    arena = models.CharField(max_length=50)
    website = models.URLField()
    logo = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    flag = models.URLField(blank=True)



    def get_absolute_url(self):
        return reverse('teams:team', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # If there is not already a slug in place...
        if not self.slug:
            # Import django's builtin slug function
            from django.template.defaultfilters import slugify
            # Call this slug function on the field you want the slug to be made of
            self.slug = slugify(self.name)
        # Call the rest of the old save() method
        super(Team, self).save(*args, **kwargs)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    number = models.IntegerField()
    height = models.IntegerField()
    born = models.IntegerField()
    nationality = models.CharField(max_length=50)
    pic = models.URLField()
    club = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    flag = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('teams:player', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        # If there is not already a slug in place...
        if not self.slug:
            # Import django's builtin slug function
            from django.template.defaultfilters import slugify
            # Call this slug function on the field you want the slug to be made of
            self.slug = slugify([self.first_name, self.last_name])
        # Call the rest of the old save() method
        super(Player, self).save(*args, **kwargs)


class Game(models.Model):
    round = models.IntegerField(null=True, blank=True)
    home_team = models.ForeignKey(Team, related_name='Home', on_delete=models.CASCADE, null=True, blank=True)
    home_result = models.IntegerField(null=True, blank=True)
    away_team = models.ForeignKey(Team, related_name='Away', on_delete=models.CASCADE, null=True, blank=True)
    away_result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return 'Round {} ({}-{})'.format(self.round, self.home_team, self.away_team)

    class Meta:

        ordering = ['-round']
