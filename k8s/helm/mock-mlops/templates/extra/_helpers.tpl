{{- define "extra-hostname" -}}
{{- $environment := default "production" .Values.ingress.environment -}}
{{- $hostname := default "cluster.local" .Values.ingress.hostname -}}
{{- $branch := default "main" .Values.ingress.branch -}}
{{- if eq $environment "production" }}
{{- printf "%s.%s" "extra" $hostname }}
{{- else if eq $environment "testing" }}
{{- printf "%s.%s" "extra.test" $hostname }}
{{- else -}}
{{- printf "%s.%s.%s" "extra" $branch $hostname }}
{{- end }}
{{- end }}


{{- define "mock-mlops.extra.labels" -}}
helm.sh/chart: {{ include "mock-mlops.chart" . }}
{{ include "mock-mlops.extra.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "mock-mlops.extra.selectorLabels" -}}
app.kubernetes.io/name: {{ include "mock-mlops.name" . }}-extra
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}