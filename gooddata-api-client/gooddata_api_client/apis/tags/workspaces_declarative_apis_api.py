# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from gooddata_api_client.paths.api_v1_layout_workspaces_workspace_id.get import GetWorkspaceLayout
from gooddata_api_client.paths.api_v1_layout_workspaces.get import GetWorkspacesLayout
from gooddata_api_client.paths.api_v1_layout_workspaces_workspace_id.put import PutWorkspaceLayout
from gooddata_api_client.paths.api_v1_layout_workspaces.put import SetWorkspacesLayout


class WorkspacesDeclarativeAPIsApi(
    GetWorkspaceLayout,
    GetWorkspacesLayout,
    PutWorkspaceLayout,
    SetWorkspacesLayout,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
