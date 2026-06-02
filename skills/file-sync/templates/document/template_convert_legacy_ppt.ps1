param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

$powerpoint = $null
$presentation = $null

try {
    $powerpoint = New-Object -ComObject PowerPoint.Application
    $powerpoint.Visible = -1

    $presentation = $powerpoint.Presentations.Open($InputPath, $false, $false, $false)
    $presentation.SaveAs($OutputPath, 24)
    Write-Output "Converted legacy PPT to PPTX."
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
finally {
    if ($presentation -ne $null) {
        $presentation.Close()
    }
    if ($powerpoint -ne $null) {
        $powerpoint.Quit()
    }
}
