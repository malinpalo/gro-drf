# **GRO-DRF**

# Testing

## Table of Contents

* [**Testing**](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Manual Testing](<#manual-testing>)
    * [Known Bugs](<#known-bugs>)

## Code Validation 

### PEP8

The GRO-DRF has been passed through the internal PEP8 validation tests.

### gro_api files

* permissions.py - No problems or warnings found
* serializers.py - No problems or warnings found
* views.py - No problems or warnings found
* models.py - No problems or warnings found
* urls.py - No problems or warnings found

### Comments App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Contact App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Followers App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Likes App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Posts py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Profiles App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

## Manual testing 

| Status | **Comments**
|:-------:|:--------|
| &check; | Can list comments
| &check; | Logged out user can't create comment
| &check; | Logged in user can create comment
| &check; | Can retrieve comment using valid ID
| &check; | Can't retrieve comment using invalid ID
| &check; | Can update own comment
| &check; | Can't update someone else's comment
| &check; | Can delete own comment
| &check; | Can't delete someone else's comment

| Status | **Contact**
|:-------:|:--------|
| &check; | Can list contacts
| &check; | Logged out user can't create contact
| &cross; | Logged in user can create contact
| &check; | Can't update someone else's contact
| &check; | Can delete own contact
| &check; | Can't delete someone else's contact

| Status | **Followers**
|:-------:|:--------|
| &check; | Can list followers
| &check; | Logged out user can't follow
| &check; | Logged in user can follow
| &check; | Can retrieve followers using valid ID
| &check; | Can't retrieve followers using invalid ID
| &check; | Can delete follow from my own profile
| &check; | Can't delete someone else's follow
| &check; | Can't follow the same profile twice

| Status | **Likes**
|:-------:|:--------|
| &check; | Can list Likes
| &check; | Logged out user can't create likes
| &check; | Logged in user can create likes
| &check; | Can retrieve likes using valid ID
| &check; | Can't retrieve likes using invalid ID
| &check; | Can delete own likes
| &check; | Can't delete someone else's likes
| &check; | Can't post likes to the same event twice

| Status | **Posts**
|:-------:|:--------|
| &check; | Can list posts
| &check; | Logged out user can't create posts
| &check; | Logged in user can create posts
| &check; | Can retrieve posts using valid ID
| &check; | Can't retrieve posts using invalid ID
| &check; | Can update own post
| &check; | Can't update someone else's post
| &check; | Can delete own post
| &check; | Can't delete someone else's post

| Status | **Profiles**
|:-------:|:--------|
| &check; | Profile automatically created on user creation
| &check; | Can list profiles
| &check; | Can retrieve profile using valid ID
| &check; | Can't retrieve profile using invalid ID
| &check; | Can update own profile
| &check; | Can't update someone else's profile
| &check; | Can delete own profile
| &check; | Can't delete someone else's profile

## Known Bugs

### Resolved bugs

Please click [**_here_**](README.md) to return to the Happening API README file.