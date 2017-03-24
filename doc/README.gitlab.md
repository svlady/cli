## GitLab CLI configuration

The CLI tool requires two parameters for accessing GitLab API endpoint:

* `GITLAB_API` - the API endpoint URL
* `GITLAB_TOKEN` - the authentication token issued by the GitLab user. Your API calls will be impersonated as this user, who issued the token. Obviously, the user must be given sufficient permissions for performing management actions on GitLab objects.

These parameters are usually provided as shell environment variables. However, for additional security, you may want to fetch the token from Vault. For this you need to have Vault up and running. See configuration example inside the `gitlab` script, in comments.

```shell
GITLAB_API=https://gitlab.local/api/v3
GITLAB_TOKEN=xxxxxxxxxxxxxxxxx
export GITLAB_API GITLAB_TOKEN
```

You can perform this configuration once in your current shell or add these variables to your shell or environment intialization files.

## Setting up shell auto-completion

The corresponding `.auto` file contains shell auto-completion function, which is providing hints and simplifies command line entry a great deal. For activation just source provided file as shown in the example below. Alternatively, you can setup auto-completion permanently by adding this command to your shell initialization script or otherwise setup autocompletion as described in your distribution documentation.

```shell
$ source gitlab.auto # replace 'source' with '.' (no quotes) if you tired typing, those two are synonyms 
```

## CLI Usage

The CLI tool is operating on _objects_ by calling _actions_ for those _objects_. For each _action_ the user may provide additional input parameters. Some _actions_ also supporting the `--format` output parameter, which is specifying resulting output format.

```shell
$ ./gitlab
GitLab CLI management tool
Usage: ./gitlab <object> <action> [<args 1> ... <arg N>]
Objects and actions:
    group <list|add|del|users|adduser|deluser> <args...>
        list (dir) [--pattern <pattern>] [--format <list|table>]
        add (create) --group <group name> [--description <description>]
        del (remove) --group <group name>
        users (members) --group <group name> [--format <list|table>]
        adduser (useradd) --group <group name> --login <user login> [--access <guest|reporter|developer|master|owner>]
        deluser (userdel) --group <group name> --login <user login>

    project <list|add|del> <args...>
        list (dir) [--group <group name>] [--pattern <pattern>] [--format <list|table>]
        add (create) --project <project name> --group <project group> [--description <project description>]
        del (remove) --project <project name> --group <project group>

    user <list|add|del> <args...>
        list (dir) [--pattern <pattern>] [--format <list|table>]
        add (create) --login <user login> --name <First Last> --mail <email> --org <LDAP org>
        del (remove) --login <user login>

```

## Examples

The CLI tool usage is pretty straightforward and below you can see several examples for performing basic management actions.

### List GitLab groups

GitLab places projects in so called groups, sometimes also called namespaces.

```shell
$ ./gitlab group list
images
poc
$
```

Results displayed as a list of records by default. The next command changes output format to table.

```shell
$ ./gitlab group list --format table
7	Private	images	https://gitlab.local/groups/images	Group for all container images
3	Private	vzpoc	https://gitlab.local/groups/poc		POC Projects
$
```

### Add new GitLab group

```shell
$ ./gitlab group add --group devops --description "DevOps related projects"
{
  "id": 134,
  "name": "devops",
  "path": "devops",
  "description": "DevOps related projects",
  "visibility_level": 0,
  "avatar_url": null,
  "web_url": "https://gitlab.local/groups/devops"
}
gitlab: successfully added group "devops"
$
```

### Add new GitLab project

```shell
$ ./gitlab project add --project devtest --group devops --description "Test harness"
{
  "id": 149,
  "description": "Test harness",
  "default_branch": null,
  "tag_list": [],
  "public": false,
  "archived": false,
  "visibility_level": 0,
  "ssh_url_to_repo": "ssh://git@gitlab.local:2222/devops/devtest.git",
  "http_url_to_repo": "https://gitlab.local/devops/devtest.git",
  "web_url": "https://gitlab.local/devops/devtest",
  "name": "devtest",
  "name_with_namespace": "devops / devtest",
  "path": "devtest",
  "path_with_namespace": "devops/devtest",
  "issues_enabled": true,
  "merge_requests_enabled": true,
  "wiki_enabled": true,
  "builds_enabled": true,
  "snippets_enabled": false,
  "created_at": "2017-03-23T15:54:28.681Z",
  "last_activity_at": "2017-03-23T15:54:31.188Z",
  "shared_runners_enabled": true,
  "creator_id": 7,
  "namespace": {
    "id": 134,
    "name": "devops",
    "path": "devops",
    "owner_id": null,
    "created_at": "2017-03-23T15:51:21.465Z",
    "updated_at": "2017-03-23T15:51:21.465Z",
    "description": "DevOps related projects",
    "avatar": {
      "url": null
    },
    "share_with_group_lock": false,
    "visibility_level": 0
  },
  "avatar_url": null,
  "star_count": 0,
  "forks_count": 0,
  "open_issues_count": 0,
  "runners_token": "xnbvapsd-azKpAmLtbsR",
  "public_builds": true
}
gitlab: project created successfully
$
```

### List GitLab users

```shell
$ ./gitlab user list --format table
41	active	jlee	Jane Lee	jlee@poc.local	ldapmain	CN=Jane Lee,OU=Star Agency,OU=EXT,OU=HOSTING,DC=LOCAL
33	active	jdoe	John Doe	jdoe@poc.local	ldapmain	CN=John Doe,OU=Star Agency,OU=EXT,OU=HOSTING,DC=LOCAL
$
```
