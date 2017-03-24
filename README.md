![CLI Tools](https://raw.githubusercontent.com/svlady/cli/master/doc/cli-logo.png)

This project contains CLI tools enabling automation, scripting and programmatic management for such applications as [GitLab](https://about.gitlab.com/), [SonarQube](https://www.sonarqube.org/), [MS Active Directory](https://msdn.microsoft.com/en-us/library/cc223122.aspx), [HashiCorp Vault](https://www.vaultproject.io/), etc. These CLI tools are operating on _objects_ and calling certain _actions_ for those _objects_, taking user inputs as parameters. Each CLI tool is performing the following basic tasks:

* Collects required and optional arguments via command line parameters
* Validates provided arguments against defined rules and patterns
* Performs additional sanity checks and complex parameter validation
* Translates arguments (object, action, parameters) into API call
* Invokes Application (Service) APIs using specified credentials
* Collects API call results and handles errors and exceptions
* Filters and formats results as requested

The project is attempting to minimize reliance on external tools and reduce number of dependencies, however, the following packages (or binaries) are required for proper operation:

* [curl](https://curl.haxx.se/) - the URL querying tool. Most probably you have it already installed, otherwise, pretty much all modern distributions providing a package that may be deployed by your distribution package manager.
* [jq](https://stedolan.github.io/jq/) - lightweight and flexible JSON processor. It could have been avoided, but it makes JSON processing tasks so that much easier and installation is so simple that it may be considered as a must have tool.
* [adtool](https://gp2x.org/adtool/) - is a unix command line utility for Active Directory administration. Obviously, it's only required by AD management tool. Although it's possible to use this tool standalone, the ldap wrapper tool adds safety and convenience.

## Installation
As simple as it gets, just place package contents under preferred deployment root and set `CLI_HOME` environment variable pointing to this location. By default, the `/opt/cli` deployment location is assumed, if `CLI_HOME` variable is not set.

```shell
$ git clone https://github.com/svlady/cli /opt/cli
$ export CLI_HOME=/opt/cli # this deployment path is assumed by default, so this command is not really required
```

Additional settings, such as API endpoints and authentication credentials and tokens are also provided via environment variables. For configuration and usage details see documentation for the corresponding tool.

### curl
In case if `curl` is not installed, use your distribution package manager to deploy this tool. Alternatively, you can download and deploy package for your OS manually using [curl download wizard](https://curl.haxx.se/dlwiz/?type=bin)

### jq
The `jq` tool is available in package repositories for most popular distributions. Please use your distribution package manager to deploy this package. Alternatively, you can follow instructions and download self-contained drop-in binary for your OS from the [jq download page](https://stedolan.github.io/jq/download/)

### adtool
The [original project page](https://gp2x.org/adtool/) does only provide source code and build instructions. You can either download and build project from original location or use patched code-base and binaries from a [local github repository](https://github.com/svlady/adtool)

## Project contents

The following files included into this project:

* `genUid.py` - short, monotonically increasing ID generator. The algorithm converts current time in milliseconds into a 7-char Base66 string. No collisions expected with process concurrency level of <1000 calls/second. This tool may be used for creating distinct user or database names, when registering new accounts. This is a drop-in tool requiring only Python interpreter. No further configuration required.
* `gitlab` - CLI tool for managing GitLab users, projects and namespaces. See [gitlab CLI documentation page](doc/README.gitlab.md) for more details.
* `gitlab.auto` - shell auto-completion function for the gitlab tool.
* `ldap` - CLI tool for managing MS Active Directory objects: OUs, Groups and Accounts. See [ldap CLI documentation page](doc/README.ldap.md) for more details.
* `ldap.auto` - shell auto-completion function for the ldap tool.
* `sonar` - CLI tool for managing SonarQube project templates, projects, groups and users. See [sonar CLI documentation page](doc/README.sonar.md) for more details.
* `sonar.auto` - shell auto-completion function for the sonar tool.
* `vault` - CLI tool for querying and managing secure credential stored in Vault. See [vault CLI documentation page](doc/README.vault.md) for more details.
* `cli.lib` - it's a shell library providing implementation for common functions utilized by CLI tools.
