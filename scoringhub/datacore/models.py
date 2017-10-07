from __future__ import unicode_literals
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Club(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Club'


class Clubhasshooter(models.Model):
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubID')  # Field name made lowercase.
    shooterid = models.ForeignKey('Shooter', models.DO_NOTHING, db_column='ShooterID')  # Field name made lowercase.
    membersince = models.DateTimeField(db_column='MemberSince', blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    activeuntil = models.DateTimeField(db_column='ActiveUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClubHasShooter'
        unique_together = (('clubid', 'shooterid'),)


class Course(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Game(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    targetcount = models.IntegerField(db_column='TargetCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Game'


class League(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clubid = models.IntegerField(db_column='ClubID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(db_column='Fee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'League'


class Leaguehasgame(models.Model):
    leagueid = models.ForeignKey(League, models.DO_NOTHING, db_column='LeagueID')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    rounds = models.IntegerField(db_column='Rounds', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeagueHasGame'
        unique_together = (('leagueid', 'gameid'),)


class Leaguehasteam(models.Model):
    leagueid = models.ForeignKey(League, models.DO_NOTHING, db_column='LeagueID')  # Field name made lowercase.
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeagueHasTeam'
        unique_together = (('leagueid', 'teamid'),)


class Pageaccess(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PageAccess'


class Role(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'


class Rolehaspageaccess(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='Role_ID')  # Field name made lowercase.
    pageaccess = models.ForeignKey(Pageaccess, models.DO_NOTHING, db_column='PageAccess_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleHasPageAccess'
        unique_together = (('role', 'pageaccess'),)


class Round(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamID', blank=True, null=True)  # Field name made lowercase.
    leagueid = models.ForeignKey(League, models.DO_NOTHING, db_column='LeagueID', blank=True, null=True)  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Round'


class Scorecard(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shooter = models.ForeignKey('Shooter', models.DO_NOTHING, db_column='Shooter_ID')  # Field name made lowercase.
    round = models.ForeignKey(Round, models.DO_NOTHING, db_column='Round_ID')  # Field name made lowercase.
    station = models.ForeignKey('Station', models.DO_NOTHING, db_column='Station_ID')  # Field name made lowercase.
    station_targetnumber = models.IntegerField(db_column='Station_TargetNumber')  # Field name made lowercase.
    targethit = models.SmallIntegerField(db_column='TargetHit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScoreCard'


class Shooter(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='StreetAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=45)  # Field name made lowercase.
    nscanumber = models.CharField(db_column='NSCANumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shooter'


class Shooterhasrole(models.Model):
    shooterid = models.ForeignKey(Shooter, models.DO_NOTHING, db_column='ShooterID')  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShooterHasRole'
        unique_together = (('shooterid', 'roleid'),)


class Shooterhasround(models.Model):
    shooterid = models.ForeignKey(Shooter, models.DO_NOTHING, db_column='ShooterID')  # Field name made lowercase.
    roundid = models.ForeignKey(Round, models.DO_NOTHING, db_column='RoundID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShooterHasRound'
        unique_together = (('shooterid', 'roundid'),)


class Station(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    targetnumber = models.IntegerField(db_column='TargetNumber')  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='GameID')  # Field name made lowercase.
    clubid = models.IntegerField(db_column='ClubID')  # Field name made lowercase.
    targettype = models.ForeignKey('Targettype', models.DO_NOTHING, db_column='TargetType_ID')  # Field name made lowercase.
    courseid = models.IntegerField(db_column='CourseID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Station'
        unique_together = (('id', 'targetnumber'),)


class Targettype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TargetType'


class Team(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    haspaid = models.SmallIntegerField(db_column='HasPaid', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Team'


class Teamhasshooter(models.Model):
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='TeamID')  # Field name made lowercase.
    shooterid = models.ForeignKey(Shooter, models.DO_NOTHING, db_column='ShooterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeamHasShooter'
        unique_together = (('teamid', 'shooterid'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
