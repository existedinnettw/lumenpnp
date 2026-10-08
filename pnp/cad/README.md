# LumenPnP FreeCAD model

The CAD of the [LumenPnP](../../README.md) pick and place machine: `assembly.FCStd` and the parts it links. Hardware designs here are available under the CERN-OHL-W v2 license; see [LICENSE](LICENSE) for the Opulo branding and trademark terms.

## Opening with fcppm

The workbenches the documents need are locked per project by [fcppm](https://github.com/existedinnettw/fcppm): A2plus (`assembly.FCStd`), Fasteners and the Honeycomb macro (`FDM/control-box.FCStd`). No Addon Manager install is needed. fcppm and the `freecad-*` packages (packaged by [fcppm_recipes](https://github.com/existedinnettw/fcppm_recipes)) come from the `inkr` Gitea index (`https://gitea.insleker.org/api/packages/inkr_org/pypi/simple/`, configured in `~/.config/uv/uv.toml` or `UV_INDEX`; log in once with `uv auth login gitea.insleker.org`). Versions are pinned in `uv.lock`.

```bash
cd pnp/cad
uv sync --locked
uv run fcppm sync                    # 3rd/freecad-*, FreeCAD.cfg
uv run fcppm run assembly.FCStd      # FreeCAD with the locked workbenches
```

## Using the model in another project

The model is published to the same index as the fcppm package `lumenpnp`: this directory, with the workbenches as dependencies.

```bash
uv add lumenpnp
uv run fcppm sync                    # 3rd/lumenpnp, 3rd/freecad-*
uv run fcppm run 3rd/lumenpnp/assembly.FCStd
```

Link its documents from your own assembly through `3rd/lumenpnp/…`.

## Releasing

Set `[project].version` in `pyproject.toml`, merge, and push the tag `vX.Y.Z` (PEP 440, e.g. `v4.1.0.post1`). `.github/workflows/fcppm-release.yml` checks the tag against the version, runs the CI checks, publishes sdist and wheel to the index and attaches them to a GitHub release. The `GITEA_PYPI_*` secrets are pushed to this repo by git-acc-rtn's secret-sync workflow.
