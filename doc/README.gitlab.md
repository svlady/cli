## gitlab CLI configuration

The CLI tool requires two parameters for accessing GitLab API endpoint:

* `GITLAB_API` - the API endpoint URL
* `GITLAB_TOKEN` - the authentication token issued for GitLab user. You API calls will be impersonated as this user, who issued the token. Obviously, the user must be given sufficient permissions for performing management actions on GitLab objects.

These parameters are usually provided as shell environment variables. However, for additional security, you may want to fetch the token from Vault. For this you need to have Vault up and running. See configuration example inside the `gitlab` script, in comments.

```shell
GITLAB_API=https://gitlab.local/api/v3
GITLAB_TOKEN=xxxxxxxxxxxxxxxxx
export GITLAB_API GITLAB_TOKEN
```

You can perform this configuration once in your current shell or add these variables to your shell or environment intialization files.

## Setting up shell auto-completion

There is a bash shell auto-completion function provided, which is providing hints and simplifies command line entry a great deal. Just source provided file as shown in example below. Alternatively, you can setup auto-completion permanently by adding this command to your shell initialization script.

```shell
$ source gitlab.auto # replace 'source' with '.' (no quotes) if you tired typing, those two are synonyms 
```

## CLI Usage

The CLI tool is operating on _objects_ by calling _actions_ for those _objects_. For each _action_ the user may provide additional input parameters.

```shell
$  ./gitlab
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