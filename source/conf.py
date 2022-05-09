# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from get_rst_files import get_files

# -- Project information -----------------------------------------------------

project = "cf-docs"
copyright = "2021, CloudFerro"
author = "CloudFerro"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

urls_dict = get_files(
    [     
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Kubernetes-Cluster-Using-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Kubernetes-Cluster-Template-Using-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Install-OpenStack-and-Magnum-Clients-for-Command-Line-Interface-to-Eumetsat-Elasticity-Horizon",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Use-Command-Line-Interface-for-Kubernetes-Clusters-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Access-Kubernetes-Cluster-Post-Deployment-Using-Kubectl-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-API-Server-LoadBalancer-for-Kubernetes-Cluster-On-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-Floating-IP-for-Servers-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Creating-Additional-Nodegroups-in-Kubernetes-Cluster-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Autoscaling-Kubernetes-Cluster-Resources-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Connect-Two-Instances-Through-a-Private-Network-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-To-Create-and-Manage-Networks-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-a-Router-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Use-Security-Groups-to-Tighten-Security-Using-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/How-to-Create-and-Return-a-Floating-IP-Address-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/kubernetes-doc/blob/main/source/Volume-based-vs-Ephemeral-based-Storage-for-Kubernetes-Clusters-on-Eumetsat-Elasticity-OpenStack-Magnum",
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/accessusings3cmd",     
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/attachvolumetovmlessthan2tb",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/cannotaccesseodata",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/ephemeralvspersistentstorage",
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/exportvolumenfs",
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/exportvolumeovernfs",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/extendvolumelinux",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/howmanyobjectsobjectstorage",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/howtoaccesseodata",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/howtomountdriveoverssh",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/mountobjectstoragelinux",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/moveadatavolume",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/volumesnapshotinheritanceanditsconsequences",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/datavolume/volumesnapshot",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/accesslisteousingboto3",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/cantaccesseodata",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/downloadeodatausingboto3",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/eodataaccess",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/eodatagoofys",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/eodatas3fs",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/mounteodatausings3protocol",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/eodata/s3cmd-download",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/accessvmfromconsole",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/clonevm",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/fixconsole",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/howtocreatenewlinuxgpu",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/howtousedocker",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/howtousesecuritygroupsinhorizon",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/keypairopenstack",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/newlinuxvm",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/openstackdomain",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/openstackproject",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/pythonvirtualenv",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/startavmfromasnapshot",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/statuspower",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/uploadimageusingopcli",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/vmnewvolumeno",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/vmnewvolumeyes",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/general/volumesnapshotinheritance",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/accessvmsusingnames",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/addremovefip",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/cannotaccess",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/cantpingvm",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/connectviasshlinux",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/connectviasshwin",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/createanetworkwithrouter",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/opennewports",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/sshkeypair",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/sshkeywebconsole",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/vmvisible",   
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/networking/vpnaas",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/backupaninstance",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/createasetofvms",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/newprojectopenstack",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/openstackcli/openstacklinux",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/deletelargebucket",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/generateec2",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/mountobjectstorage",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/objectstorage",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/remotetransfer",  
       "https://github.com/CloudFerro/cf3-doc/blob/main/source/s3/s3fscache",
        
    ]
)

html_context = {
    "display_github": True,
    "urls_dict": urls_dict,
    "github_host": "github.com",
    "github_user": "CloudFerro",
    "github_repo": "waw3-1-kubernetes-test",
    "github_version": "main",
    "conf_py_path": "/source/",
    "source_suffix": ".rst",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

