AWS Cli - Useful commands
=========================


Setup Auto completion

.. tabs::

    .. tab:: MacOS

        .. code-block:: bash

            # Install awscli using brew
            $ brew install awscli
            
            # Run this command to add the completion to your .zshrc file
            $ autoload -Uz compinit && compinit

            # Add the following line to your .zshrc file
            if type aws_completer &>/dev/null; then
                complete -C "$(command -v aws_completer)" aws
            fi
            $ source ~/.zshrc

    .. tab:: Linux

        .. code-block:: bash
            
            # Install awscli using yum
            $ yum install -y awscli

            # AWS CLI autocompletion. Add the following lines to your .bashrc file
            if [ -x "$(command -v aws_completer)" ]; then
                complete -C "$(command -v aws_completer)" aws
            fi

            # Source the bashrc file
            $ source ~/.bashrc

    .. tab:: Windows

        .. code-block:: powershell

            # Download the AWS CLI MSI installer for Windows
            # You can download it from the AWS CLI User Guide or use the following URL:
            # https://awscli.amazonaws.com/AWSCLIV2.msi

            # Run the downloaded MSI installer

            # AWS CLI autocompletion
            # AWS CLI v2 comes with built-in autocompletion. It should work out of the box in PowerShell.

.. details:: Route53

    .. list-table::
        :widths: 60 40
        :header-rows: 1

        * - Command
          - Description*
        * - aws route53 list-hosted-zones
          - List all hosted zones.
        * - aws route53 create-hosted-zone --name example.com --caller-reference 1234567890
          - Create a new hosted zone with the specified name and caller reference.
        * - aws route53 delete-hosted-zone --id Z1234567890
          - Delete the hosted zone with the specified ID.
        * - aws route53 change-resource-record-sets --hosted-zone-id Z1234567890 --change-batch file://change_batch.json
          - Change resource record sets in the specified hosted zone using the change batch file.
        * - aws route53 get-hosted-zone --id Z1234567890
          - Get information about the hosted zone with the specified ID.
        