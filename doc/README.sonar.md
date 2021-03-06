## Sonar CLI configuration

The CLI tool requires several parameters for its function

* `SONAR_URL` - the API endpoint URL
* `SONAR_TOKEN` - the authentication token issued by the Sonar user. Your API calls will be impersonated as this user, who issued the token. Obviously, the user must be given sufficient permissions for performing management actions on Sonar objects. The API authentication is also possible with username and password, however, the token is considered to be better and more secure approach.

These parameters are usually provided as shell environment variables. However, for additional security, you may want to fetch the bind password from Vault. For this you need to have Vault up and running. See configuration example inside the `sonar` script, in comments.

```shell
SONAR_URL="http://sonar.local:9000"
SONAR_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export SONAR_URL SONAR_TOKEN
```

You can perform this configuration once in your current shell or add these variables to your shell or environment intialization files.

## Setting up shell auto-completion

The corresponding `.auto` file contains shell auto-completion function, which is providing hints and simplifies command line entry a great deal. For activation just source provided file as shown in the example below. Alternatively, you can setup auto-completion permanently by adding this command to your shell initialization script or otherwise setup autocompletion as described in your distribution documentation.

```shell
$ source sonar.auto # replace 'source' with '.' (no quotes) if you tired typing, those two are synonyms 
```

## CLI Usage

The CLI tool is operating on _objects_ by calling _actions_ for those _objects_. For each _action_ the user may provide additional input parameters. Some _actions_ also supporting the `--format` output parameter, which is specifying resulting output format.

```shell
$ ./sonar
SonarQube CLI tool for managing projects and permissions
Usage: ./sonar <object> <action> [<args 1> ... <arg N>]
Objects and actions:
    group <list|add|del> <args...>
        list (dir) [--pattern <pattern>] [--format <list|table>]
        add (create) --group <group name> [--description <description>]
        del (remove) --group <group name> | --gid <group id>

    project <list|del> <args...>
        list (dir) [--key <project key prefix>] [--pattern <pattern>]
        del (remove) --key <project key prefix>

    template <list|add|del|groups|addgroup|delgroup|permissions> <args...>
        list (dir) [--pattern <pattern>] [--format <list|table>]
        add (create) --template <template name> --key <project pattern> [--description <project description>]
        del (remove) --template <template name> | --tid <template id>
        groups --template <template name> | --tid <template id> --permission <user, admin, issueadmin, codeviewer, scan>
        addgroup --template <template name> --group <group name> --permission <user, admin, issueadmin, codeviewer, scan>
        delgroup --template <template name> --group <group name> --permission <user, admin, issueadmin, codeviewer, scan>
        permissions

```

## Examples

The CLI tool usage is pretty straightforward and below you can see several examples for performing basic management actions.

### List Sonar template permissions

```shell
$ ./sonar template permissions
{
  "key": "user",
  "name": "Browse",
  "description": "Access a project, browse its measures, and create/edit issues for it."
}
{
  "key": "admin",
  "name": "Administer",
  "description": "Access project settings and perform administration tasks. (Users will also need \"Browse\" permission)"
}
{
  "key": "issueadmin",
  "name": "Administer Issues",
  "description": "Perform advanced editing on issues: marking an issue False Positive / Won't Fix, and changing an Issue's severity. (Users will also need \"Browse\" permission)"
}
{
  "key": "codeviewer",
  "name": "See Source Code",
  "description": "View the project's source code. (Users will also need \"Browse\" permission)"
}
{
  "key": "scan",
  "name": "Execute Analysis",
  "description": "Ability to get all settings required to perform an analysis (including the secured settings like passwords) and to push analysis results to the SonarQube server."
}
$
```

### List Sonar template groups and their permissions

As you can see from example below the project template assigned to Sonar projects by default grants `user` permissions to `Anyone`, thus allowing any user to access a project, browse its measures, and create/edit issues for it. Consider using different, more sepcific template in real life scenarios.
 
```shell
$ ./sonar template list --format table
default_template		Default template	This permission template will be...
$ ./sonar template groups --tid default_template --permission user
Anyone
$
```

### Add new Sonar template

Creating new Sonar template includes multiple steps:

* creating AD/LDAP user group that will used for SonarQube authorization
* creating SonarQube authorization group, which is mapped to the corresponding LDAP group
* creating SonarQube permission template to tie together user, groups and their permissions
* updating template by granting certain permissions to the corresponding user group

Below is an example for the steps outlined above.

#### Adding LDAP authorization group
```shell
$ ./ldap group add --group "Star Agency Sonar Users"
ldap: successfully added group "Star Agency Sonar Users"
$
```

#### Creating SonarQube authorization group
```shell
$ ./sonar group add --group "Star Agency Sonar Users"
{
  "group": {
    "id": "19",
    "name": "Star Agency Sonar Users",
    "description": "Star Agency Sonar Users project group",
    "membersCount": 0
  }
}
sonar: successfully added group "Star Agency Sonar Users"
$
```

#### Creating SonarQube permission template
```shell
$ ./sonar template add --template "Star Agency" --key "star_agency:*"
{
  "permissionTemplate": {
    "id": "AVm3JP0A8bCpdL7FQOOT",
    "name": "Star Agency",
    "description": "Star Agency permissions",
    "projectKeyPattern": "star_agency:*",
    "createdAt": "2017-01-19T14:32:51+0000",
    "updatedAt": "2017-01-19T14:32:51+0000",
    "permissions": []
  }
}
$
```

#### Adding SonarQube "Browse" permission to the template

```shell
$ ./sonar template addgroup --template "Star Agency" --group "Star Agency Sonar Users" --permission "user"
sonar: permission template updated successfully
$
```

#### Adding SonarQube "See Source Code" permission to the template

```shell
$ ./sonar template addgroup --template "Star Agency" --group "Star Agency Sonar Users" --permission "codeviewer"
sonar: permission template updated successfully
$
```
